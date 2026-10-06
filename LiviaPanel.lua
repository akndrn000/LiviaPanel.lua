local Players = game:GetService("Players")
local CoreGui = game:GetService("CoreGui")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local UIS = game:GetService("UserInputService")

local LP = Players.LocalPlayer

-- ==========================================
-- REMOVE PREVIOUS VERSION
-- ==========================================

if _G.LiviaCleanup then
    pcall(_G.LiviaCleanup)
end

local old = CoreGui:FindFirstChild("LiviaPanel")
if old then
    old:Destroy()
end

-- ==========================================
-- CONFIG
-- ==========================================

local State = {
    Speed = false,
    Jump = false,
    Fly = false
}

local Value = {
    Speed = 50,
    Jump = 100,
    Fly = 60
}

-- ==========================================
-- COLORS
-- ==========================================

local C = {
    Background = Color3.fromRGB(14, 15, 21),
    Header = Color3.fromRGB(23, 25, 34),
    Row = Color3.fromRGB(28, 31, 43),
    Input = Color3.fromRGB(39, 43, 59),

    Border = Color3.fromRGB(55, 59, 78),

    Accent = Color3.fromRGB(124, 92, 255),
    Active = Color3.fromRGB(46, 204, 133),
    Inactive = Color3.fromRGB(67, 72, 94),
    Close = Color3.fromRGB(235, 80, 92),

    Text = Color3.fromRGB(242, 243, 248),
    SubText = Color3.fromRGB(160, 164, 178)
}

-- ==========================================
-- HELPERS
-- ==========================================

local function makeCorner(object, radius)
    local corner = Instance.new("UICorner")
    corner.CornerRadius = UDim.new(0, radius)
    corner.Parent = object
    return corner
end

local function makeStroke(object)
    local stroke = Instance.new("UIStroke")
    stroke.Color = C.Border
    stroke.Thickness = 1
    stroke.Transparency = 0.15
    stroke.Parent = object
    return stroke
end

local function create(className, parent)
    local object = Instance.new(className)
    object.Parent = parent
    return object
end

-- ==========================================
-- CHARACTER
-- ==========================================

local function getCharacter()
    local character = LP.Character

    if not character then
        return nil, nil, nil
    end

    local humanoid = character:FindFirstChildOfClass("Humanoid")
    local root = character:FindFirstChild("HumanoidRootPart")

    return character, humanoid, root
end

-- ==========================================
-- FLY
-- ==========================================

local bodyVelocity
local bodyGyro

local function stopFly()
    if bodyVelocity then
        bodyVelocity:Destroy()
        bodyVelocity = nil
    end

    if bodyGyro then
        bodyGyro:Destroy()
        bodyGyro = nil
    end

    local _, humanoid = getCharacter()

    if humanoid then
        humanoid.PlatformStand = false
    end
end

-- ==========================================
-- APPLY FEATURE
-- ==========================================

local function applyFeature(key, enabled)
    local _, humanoid = getCharacter()

    if key == "Speed" then
        if not enabled and humanoid then
            humanoid.WalkSpeed = 16
        end
    end

    if key == "Jump" then
        if not enabled and humanoid then
            humanoid.UseJumpPower = true
            humanoid.JumpPower = 50
        end
    end

    if key == "Fly" then
        if not enabled then
            stopFly()
        end
    end
end

-- ==========================================
-- CONNECTIONS
-- ==========================================

local Connections = {}

-- ==========================================
-- FEATURE LOOP
-- ==========================================

Connections[#Connections + 1] = RunService.Heartbeat:Connect(function()
    local _, humanoid, root = getCharacter()

    if not humanoid or not root then
        return
    end

    -- SPEED
    if State.Speed then
        humanoid.WalkSpeed = Value.Speed
    end

    -- JUMP
    if State.Jump then
        humanoid.UseJumpPower = true
        humanoid.JumpPower = Value.Jump
    end

    -- FLY
    if State.Fly then
        local camera = workspace.CurrentCamera

        if not bodyVelocity or bodyVelocity.Parent ~= root then
            stopFly()

            bodyVelocity = Instance.new("BodyVelocity")
            bodyVelocity.MaxForce = Vector3.new(
                9e9,
                9e9,
                9e9
            )
            bodyVelocity.Velocity = Vector3.zero
            bodyVelocity.Parent = root

            bodyGyro = Instance.new("BodyGyro")
            bodyGyro.MaxTorque = Vector3.new(
                9e9,
                9e9,
                9e9
            )
            bodyGyro.P = 9e4
            bodyGyro.Parent = root
        end

        humanoid.PlatformStand = true

        local look = camera.CFrame.LookVector

        local horizontal = Vector3.new(
            look.X,
            0,
            look.Z
        )

        if horizontal.Magnitude > 0 then
            horizontal = horizontal.Unit

            bodyGyro.CFrame = CFrame.lookAt(
                root.Position,
                root.Position + horizontal
            )
        end

        local direction = humanoid.MoveDirection
        local velocity = direction * Value.Fly

        if direction.Magnitude > 0
            and horizontal.Magnitude > 0 then

            local forward = direction:Dot(horizontal)

            velocity = velocity + Vector3.new(
                0,
                look.Y * forward * Value.Fly,
                0
            )
        end

        bodyVelocity.Velocity = velocity
    end
end)

-- ==========================================
-- TAP / DRAG
-- ==========================================

local DRAG_THRESHOLD = 10

local Drag = {
    Active = false
}

local function isPress(input)
    return input.UserInputType == Enum.UserInputType.MouseButton1
        or input.UserInputType == Enum.UserInputType.Touch
end

local function bindDrag(object, target, callback)
    object.InputBegan:Connect(function(input)
        if not isPress(input) then
            return
        end

        if Drag.Active then
            return
        end

        Drag = {
            Active = true,
            Input = input,
            Start = input.Position,
            Origin = target.Position,
            Target = target,
            Moved = false,
            Callback = callback
        }
    end)
end

Connections[#Connections + 1] = UIS.InputChanged:Connect(function(input)
    if not Drag.Active then
        return
    end

    local valid =
        input == Drag.Input
        or (
            input.UserInputType == Enum.UserInputType.MouseMovement
            and Drag.Input.UserInputType == Enum.UserInputType.MouseButton1
        )

    if not valid then
        return
    end

    local delta = input.Position - Drag.Start

    if not Drag.Moved then
        if delta.Magnitude > DRAG_THRESHOLD then
            Drag.Moved = true
        end
    end

    if Drag.Moved then
        local origin = Drag.Origin

        Drag.Target.Position = UDim2.new(
            origin.X.Scale,
            origin.X.Offset + delta.X,

            origin.Y.Scale,
            origin.Y.Offset + delta.Y
        )
    end
end)

Connections[#Connections + 1] = UIS.InputEnded:Connect(function(input)
    if not Drag.Active then
        return
    end

    if input ~= Drag.Input then
        return
    end

    local callback = Drag.Callback
    local wasTap = not Drag.Moved

    Drag = {
        Active = false
    }

    if wasTap and callback then
        callback()
    end
end)

-- ==========================================
-- SCREEN GUI
-- ==========================================

local ScreenGui = create("ScreenGui", CoreGui)

ScreenGui.Name = "LiviaPanel"
ScreenGui.ResetOnSpawn = false
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

-- ==========================================
-- MAIN PANEL
-- ==========================================

local Main = create("Frame", ScreenGui)

Main.Name = "Main"
Main.Size = UDim2.new(0, 245, 0, 238)
Main.Position = UDim2.new(0.5, -122, 0.5, -119)
Main.BackgroundColor3 = C.Background
Main.BorderSizePixel = 0

makeCorner(Main, 13)
makeStroke(Main)

bindDrag(Main, Main)

-- ==========================================
-- HEADER
-- ==========================================

local Header = create("Frame", Main)

Header.Name = "Header"
Header.Size = UDim2.new(1, 0, 0, 42)
Header.BackgroundColor3 = C.Header
Header.BorderSizePixel = 0

makeCorner(Header, 13)

bindDrag(Header, Main)

-- Header bottom cover
local HeaderCover = create("Frame", Header)

HeaderCover.Size = UDim2.new(1, 0, 0, 13)
HeaderCover.Position = UDim2.new(0, 0, 1, -13)
HeaderCover.BackgroundColor3 = C.Header
HeaderCover.BorderSizePixel = 0

-- Accent line
local AccentLine = create("Frame", Header)

AccentLine.Size = UDim2.new(1, 0, 0, 2)
AccentLine.Position = UDim2.new(0, 0, 1, -2)
AccentLine.BackgroundColor3 = C.Accent
AccentLine.BorderSizePixel = 0

-- ==========================================
-- TITLE
-- ==========================================

local Title = create("TextLabel", Header)

Title.Size = UDim2.new(1, -82, 1, 0)
Title.Position = UDim2.new(0, 13, 0, 0)
Title.BackgroundTransparency = 1

Title.Text = "LIVIA PANEL"
Title.Font = Enum.Font.GothamBold
Title.TextSize = 14
Title.TextColor3 = C.Text
Title.TextXAlignment = Enum.TextXAlignment.Left

-- ==========================================
-- MINIMIZE
-- ==========================================

local Minimize = create("TextButton", Header)

Minimize.Size = UDim2.new(0, 28, 0, 28)
Minimize.Position = UDim2.new(1, -65, 0.5, -14)
Minimize.BackgroundColor3 = C.Input

Minimize.Text = "−"
Minimize.Font = Enum.Font.GothamBold
Minimize.TextSize = 16
Minimize.TextColor3 = C.Text

Minimize.AutoButtonColor = false

makeCorner(Minimize, 7)

-- ==========================================
-- CLOSE
-- ==========================================

local Close = create("TextButton", Header)

Close.Size = UDim2.new(0, 28, 0, 28)
Close.Position = UDim2.new(1, -33, 0.5, -14)
Close.BackgroundColor3 = C.Close

Close.Text = "×"
Close.Font = Enum.Font.GothamBold
Close.TextSize = 17
Close.TextColor3 = C.Text

Close.AutoButtonColor = false

makeCorner(Close, 7)

-- ==========================================
-- BODY
-- ==========================================

local Body = create("Frame", Main)

Body.Size = UDim2.new(1, -20, 1, -52)
Body.Position = UDim2.new(0, 10, 0, 48)
Body.BackgroundTransparency = 1

local Layout = create("UIListLayout", Body)

Layout.Padding = UDim.new(0, 7)
Layout.SortOrder = Enum.SortOrder.LayoutOrder

-- ==========================================
-- FEATURE ROW
-- ==========================================

local function createFeatureRow(title, key, order)
    local Row = create("Frame", Body)

    Row.Name = key
    Row.LayoutOrder = order

    Row.Size = UDim2.new(1, 0, 0, 55)
    Row.BackgroundColor3 = C.Row
    Row.BorderSizePixel = 0

    makeCorner(Row, 9)
    makeStroke(Row)

    bindDrag(Row, Main)

    -- FEATURE NAME
    local Name = create("TextLabel", Row)

    Name.Size = UDim2.new(0, 65, 1, 0)
    Name.Position = UDim2.new(0, 11, 0, 0)

    Name.BackgroundTransparency = 1
    Name.Text = title

    Name.Font = Enum.Font.GothamBold
    Name.TextSize = 12
    Name.TextColor3 = C.Text

    Name.TextXAlignment = Enum.TextXAlignment.Left

    -- VALUE BOX
    local Input = create("TextBox", Row)

    Input.Size = UDim2.new(0, 55, 0, 31)
    Input.Position = UDim2.new(1, -127, 0.5, -15)

    Input.BackgroundColor3 = C.Input
    Input.BorderSizePixel = 0

    Input.Text = tostring(Value[key])
    Input.Font = Enum.Font.GothamBold
    Input.TextSize = 12
    Input.TextColor3 = C.Text

    Input.ClearTextOnFocus = false
    Input.TextXAlignment = Enum.TextXAlignment.Center

    makeCorner(Input, 7)

    Input.FocusLost:Connect(function()
        local number = tonumber(Input.Text)

        if number and number >= 0 then
            Value[key] = number
        else
            Input.Text = tostring(Value[key])
        end
    end)

    -- ON / OFF
    local Toggle = create("TextButton", Row)

    Toggle.Size = UDim2.new(0, 58, 0, 31)
    Toggle.Position = UDim2.new(1, -65, 0.5, -15)

    Toggle.BackgroundColor3 = C.Inactive
    Toggle.BorderSizePixel = 0

    Toggle.Text = "OFF"
    Toggle.Font = Enum.Font.GothamBold
    Toggle.TextSize = 11
    Toggle.TextColor3 = C.Text

    Toggle.AutoButtonColor = false

    makeCorner(Toggle, 7)

    bindDrag(Toggle, Main, function()
        State[key] = not State[key]

        Toggle.Text = State[key] and "ON" or "OFF"

        TweenService:Create(
            Toggle,
            TweenInfo.new(
                0.15,
                Enum.EasingStyle.Quad,
                Enum.EasingDirection.Out
            ),
            {
                BackgroundColor3 =
                    State[key]
                    and C.Active
                    or C.Inactive
            }
        ):Play()

        applyFeature(key, State[key])
    end)
end

-- ==========================================
-- FEATURES
-- ==========================================

createFeatureRow("SPEED", "Speed", 1)
createFeatureRow("JUMP", "Jump", 2)
createFeatureRow("FLY", "Fly", 3)

-- ==========================================
-- OPEN BUTTON
-- ==========================================

local OpenButton = create("TextButton", ScreenGui)

OpenButton.Size = UDim2.new(0, 46, 0, 46)
OpenButton.Position = UDim2.new(0, 16, 0.5, -23)

OpenButton.BackgroundColor3 = C.Accent
OpenButton.BorderSizePixel = 0

OpenButton.Text = "L"
OpenButton.Font = Enum.Font.GothamBold
OpenButton.TextSize = 19
OpenButton.TextColor3 = C.Text

OpenButton.AutoButtonColor = false
OpenButton.Visible = false

makeCorner(OpenButton, 23)

-- ==========================================
-- MINIMIZE / OPEN
-- ==========================================

bindDrag(Minimize, Main, function()
    Main.Visible = false
    OpenButton.Visible = true
end)

bindDrag(OpenButton, OpenButton, function()
    Main.Visible = true
    OpenButton.Visible = false
end)

-- ==========================================
-- CLEANUP
-- ==========================================

local function cleanup()
    State.Speed = false
    State.Jump = false
    State.Fly = false

    applyFeature("Speed", false)
    applyFeature("Jump", false)
    applyFeature("Fly", false)

    stopFly()

    for _, connection in ipairs(Connections) do
        pcall(function()
            connection:Disconnect()
        end)
    end

    Connections = {}

    if ScreenGui then
        ScreenGui:Destroy()
    end

    _G.LiviaCleanup = nil
end

_G.LiviaCleanup = cleanup

-- Close button uses direct connection
bindDrag(Close, Main, function()
    cleanup()
end)
