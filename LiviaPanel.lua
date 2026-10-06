```lua
--[[
    Livia Panel v2.0
    Speed | Jump | Fly

    Ghost dan ESP telah dihapus.
    Panel dibuat lebih kecil untuk layar HP.
]]

local Players = game:GetService("Players")
local CoreGui = game:GetService("CoreGui")
local RunService = game:GetService("RunService")
local TweenService = game:GetService("TweenService")
local UIS = game:GetService("UserInputService")

local LP = Players.LocalPlayer

-- ==========================================
-- CLEANUP PREVIOUS VERSION
-- ==========================================

if _G.LiviaCleanup then
    pcall(_G.LiviaCleanup)
end

if CoreGui:FindFirstChild("LiviaPanel") then
    CoreGui.LiviaPanel:Destroy()
end

-- ==========================================
-- STATE
-- ==========================================

local S = {
    Speed = false,
    Jump = false,
    Fly = false
}

local V = {
    Speed = 50,
    Jump = 100,
    Fly = 60
}

-- ==========================================
-- THEME
-- ==========================================

local T = {
    BG = Color3.fromRGB(16, 17, 24),
    Panel = Color3.fromRGB(24, 26, 37),
    Card = Color3.fromRGB(32, 35, 50),
    Input = Color3.fromRGB(44, 48, 68),
    Stroke = Color3.fromRGB(58, 63, 90),
    Accent = Color3.fromRGB(124, 92, 255),
    Text = Color3.fromRGB(240, 242, 250),
    Off = Color3.fromRGB(70, 75, 100),
    On = Color3.fromRGB(46, 204, 133),
    Red = Color3.fromRGB(240, 84, 96),
}

local function corner(obj, radius)
    local c = Instance.new("UICorner")
    c.CornerRadius = UDim.new(0, radius or 8)
    c.Parent = obj
    return c
end

local function stroke(obj)
    local s = Instance.new("UIStroke")
    s.Color = T.Stroke
    s.Thickness = 1
    s.Parent = obj
    return s
end

-- ==========================================
-- FEATURE LOGIC
-- ==========================================

local conns = {}

local bv
local bg

local function getChar()
    local char = LP.Character
    local hum = char and char:FindFirstChildOfClass("Humanoid")
    local hrp = char and char:FindFirstChild("HumanoidRootPart")

    return char, hum, hrp
end

local function stopFly()
    if bv then
        bv:Destroy()
        bv = nil
    end

    if bg then
        bg:Destroy()
        bg = nil
    end

    local _, hum = getChar()

    if hum then
        hum.PlatformStand = false
    end
end

local function applyChange(key, state)
    local _, hum = getChar()

    if key == "Speed" and not state then
        if hum then
            hum.WalkSpeed = 16
        end
    end

    if key == "Jump" and not state then
        if hum then
            hum.UseJumpPower = true
            hum.JumpPower = 50
        end
    end

    if key == "Fly" and not state then
        stopFly()
    end
end

-- ==========================================
-- FEATURE LOOP
-- ==========================================

conns[#conns + 1] = RunService.Heartbeat:Connect(function()
    local _, hum, hrp = getChar()

    if not hum or not hrp then
        return
    end

    -- SPEED
    if S.Speed then
        hum.WalkSpeed = V.Speed
    end

    -- JUMP
    if S.Jump then
        hum.UseJumpPower = true
        hum.JumpPower = V.Jump
    end

    -- FLY
    if S.Fly then
        local cam = workspace.CurrentCamera

        if not bv or bv.Parent ~= hrp then
            stopFly()

            bv = Instance.new("BodyVelocity")
            bv.MaxForce = Vector3.new(9e9, 9e9, 9e9)
            bv.Velocity = Vector3.zero
            bv.Parent = hrp

            bg = Instance.new("BodyGyro")
            bg.MaxTorque = Vector3.new(9e9, 9e9, 9e9)
            bg.P = 9e4
            bg.Parent = hrp
        end

        hum.PlatformStand = true

        local look = cam.CFrame.LookVector

        local flat = Vector3.new(
            look.X,
            0,
            look.Z
        )

        if flat.Magnitude > 0 then
            flat = flat.Unit

            bg.CFrame = CFrame.lookAt(
                hrp.Position,
                hrp.Position + flat
            )
        end

        local dir = hum.MoveDirection
        local vel = dir * V.Fly

        if dir.Magnitude > 0 and flat.Magnitude > 0 then
            local forward = dir:Dot(flat)

            vel = vel + Vector3.new(
                0,
                look.Y * forward * V.Fly,
                0
            )
        end

        bv.Velocity = vel
    end
end)

-- ==========================================
-- TAP / DRAG SYSTEM
-- ==========================================

local DRAG_THRESHOLD = 10

local drag = {
    active = false
}

local function isPress(input)
    return input.UserInputType == Enum.UserInputType.MouseButton1
        or input.UserInputType == Enum.UserInputType.Touch
end

local function bindDrag(obj, target, onTap)
    obj.InputBegan:Connect(function(input)
        if not isPress(input) then
            return
        end

        if drag.active then
            return
        end

        drag = {
            active = true,
            input = input,
            startPos = input.Position,
            target = target,
            origin = target.Position,
            moved = false,
            onTap = onTap
        }
    end)
end

conns[#conns + 1] = UIS.InputChanged:Connect(function(input)
    if not drag.active then
        return
    end

    local valid =
        input == drag.input
        or (
            input.UserInputType == Enum.UserInputType.MouseMovement
            and drag.input.UserInputType == Enum.UserInputType.MouseButton1
        )

    if not valid then
        return
    end

    local delta = input.Position - drag.startPos

    if not drag.moved then
        if Vector2.new(delta.X, delta.Y).Magnitude > DRAG_THRESHOLD then
            drag.moved = true
        end
    end

    if drag.moved then
        local origin = drag.origin

        drag.target.Position = UDim2.new(
            origin.X.Scale,
            origin.X.Offset + delta.X,
            origin.Y.Scale,
            origin.Y.Offset + delta.Y
        )
    end
end)

conns[#conns + 1] = UIS.InputEnded:Connect(function(input)
    if not drag.active then
        return
    end

    if input == drag.input then
        local tap = (not drag.moved) and drag.onTap

        drag = {
            active = false
        }

        if tap then
            tap()
        end
    end
end)

-- ==========================================
-- UI
-- ==========================================

local cleanup

local sg = Instance.new("ScreenGui")
sg.Name = "LiviaPanel"
sg.ResetOnSpawn = false
sg.Parent = CoreGui

-- ==========================================
-- MAIN PANEL
-- ==========================================

local Main = Instance.new("Frame")
Main.Size = UDim2.new(0, 230, 0, 270)
Main.Position = UDim2.new(0.5, -115, 0.5, -135)
Main.BackgroundColor3 = T.BG
Main.BorderSizePixel = 0
Main.Parent = sg

corner(Main, 12)
stroke(Main)

bindDrag(Main, Main)

-- ==========================================
-- HEADER
-- ==========================================

local Header = Instance.new("Frame")
Header.Size = UDim2.new(1, 0, 0, 40)
Header.BackgroundColor3 = T.Panel
Header.BorderSizePixel = 0
Header.Parent = Main

corner(Header, 12)
bindDrag(Header, Main)

local hc = Instance.new("Frame")
hc.Size = UDim2.new(1, 0, 0, 12)
hc.Position = UDim2.new(0, 0, 1, -12)
hc.BackgroundColor3 = T.Panel
hc.BorderSizePixel = 0
hc.Parent = Header

local line = Instance.new("Frame")
line.Size = UDim2.new(1, 0, 0, 2)
line.Position = UDim2.new(0, 0, 1, -2)
line.BackgroundColor3 = T.Accent
line.BorderSizePixel = 0
line.Parent = Header

-- ==========================================
-- TITLE
-- ==========================================

local Title = Instance.new("TextLabel")
Title.Size = UDim2.new(1, -80, 1, 0)
Title.Position = UDim2.new(0, 10, 0, 0)
Title.BackgroundTransparency = 1
Title.Text = "LIVIA PANEL"
Title.Font = Enum.Font.GothamBold
Title.TextSize = 14
Title.TextColor3 = T.Text
Title.TextXAlignment = Enum.TextXAlignment.Left
Title.Parent = Header

-- ==========================================
-- HEADER BUTTON
-- ==========================================

local function headBtn(x, text, color)
    local b = Instance.new("TextButton")
    b.Size = UDim2.new(0, 28, 0, 28)
    b.Position = UDim2.new(1, x, 0.5, -14)
    b.BackgroundColor3 = color
    b.Text = text
    b.Font = Enum.Font.GothamBold
    b.TextSize = 14
    b.TextColor3 = T.Text
    b.AutoButtonColor = false
    b.Parent = Header

    corner(b, 7)

    return b
end

local CloseBtn = headBtn(-34, "X", T.Red)
local MinBtn = headBtn(-68, "-", T.Input)

-- ==========================================
-- OPEN BUTTON
-- ==========================================

local OpenBtn = Instance.new("TextButton")
OpenBtn.Size = UDim2.new(0, 46, 0, 46)
OpenBtn.Position = UDim2.new(0, 15, 0.5, -23)
OpenBtn.BackgroundColor3 = T.Accent
OpenBtn.Text = "L"
OpenBtn.Font = Enum.Font.GothamBold
OpenBtn.TextSize = 20
OpenBtn.TextColor3 = T.Text
OpenBtn.AutoButtonColor = false
OpenBtn.Visible = false
OpenBtn.Parent = sg

corner(OpenBtn, 23)

-- ==========================================
-- MINIMIZE / OPEN / CLOSE
-- ==========================================

bindDrag(MinBtn, Main, function()
    Main.Visible = false
    OpenBtn.Visible = true
end)

bindDrag(OpenBtn, OpenBtn, function()
    Main.Visible = true
    OpenBtn.Visible = false
end)

bindDrag(CloseBtn, Main, function()
    cleanup()
end)

-- ==========================================
-- BODY
-- ==========================================

local Body = Instance.new("Frame")
Body.Size = UDim2.new(1, 0, 1, -40)
Body.Position = UDim2.new(0, 0, 0, 40)
Body.BackgroundTransparency = 1
Body.Parent = Main

local pad = Instance.new("UIPadding")
pad.PaddingTop = UDim.new(0, 8)
pad.PaddingLeft = UDim.new(0, 8)
pad.PaddingRight = UDim.new(0, 8)
pad.Parent = Body

local list = Instance.new("UIListLayout")
list.Padding = UDim.new(0, 7)
list.Parent = Body

-- ==========================================
-- FEATURE ROW
-- ==========================================

local function createRow(label, key)
    local row = Instance.new("Frame")

    row.Size = UDim2.new(1, 0, 0, 62)
    row.BackgroundColor3 = T.Card
    row.BorderSizePixel = 0
    row.Parent = Body

    corner(row, 9)
    stroke(row)

    bindDrag(row, Main)

    -- LABEL
    local lb = Instance.new("TextLabel")
    lb.Size = UDim2.new(0, 62, 0, 22)
    lb.Position = UDim2.new(0, 10, 0, 8)
    lb.BackgroundTransparency = 1
    lb.Text = label
    lb.Font = Enum.Font.GothamBold
    lb.TextSize = 12
    lb.TextColor3 = T.Text
    lb.TextXAlignment = Enum.TextXAlignment.Left
    lb.Parent = row

    -- VALUE BOX
    local box = Instance.new("TextBox")
    box.Size = UDim2.new(0, 48, 0, 28)
    box.Position = UDim2.new(0, 10, 1, -35)
    box.BackgroundColor3 = T.Input
    box.Text = tostring(V[key])
    box.Font = Enum.Font.GothamBold
    box.TextSize = 12
    box.TextColor3 = T.Text
    box.ClearTextOnFocus = false
    box.Parent = row

    corner(box, 7)

    box.FocusLost:Connect(function()
        local n = tonumber(box.Text)

        if n and n >= 0 then
            V[key] = n
        else
            box.Text = tostring(V[key])
        end
    end)

    -- ON / OFF BUTTON
    local btn = Instance.new("TextButton")
    btn.Size = UDim2.new(0, 62, 0, 30)
    btn.Position = UDim2.new(1, -72, 0.5, -15)
    btn.BackgroundColor3 = T.Off
    btn.Text = "OFF"
    btn.Font = Enum.Font.GothamBold
    btn.TextSize = 12
    btn.TextColor3 = T.Text
    btn.AutoButtonColor = false
    btn.Parent = row

    corner(btn, 7)

    bindDrag(btn, Main, function()
        S[key] = not S[key]

        btn.Text = S[key] and "ON" or "OFF"

        TweenService:Create(
            btn,
            TweenInfo.new(0.15),
            {
                BackgroundColor3 = S[key] and T.On or T.Off
            }
        ):Play()

        applyChange(key, S[key])
    end)
end

-- ==========================================
-- ONLY 3 FEATURES
-- ==========================================

createRow("SPEED", "Speed")
createRow("JUMP", "Jump")
createRow("FLY", "Fly")

-- ==========================================
-- CLEANUP
-- ==========================================

cleanup = function()
    for key in pairs(S) do
        if S[key] then
            S[key] = false
            applyChange(key, false)
        end
    end

    stopFly()

    for _, connection in ipairs(conns) do
        pcall(function()
            connection:Disconnect()
        end)
    end

    conns = {}

    if sg then
        sg:Destroy()
    end
end

_G.LiviaCleanup = cleanup
```
