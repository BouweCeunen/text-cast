
Param(
	[string]$name,
	[string]$msg
)

[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon 

$objNotifyIcon.Icon = $PSScriptRoot + "\msgicon.ico"
$objNotifyIcon.BalloonTipIcon = "Info" 
$objNotifyIcon.BalloonTipText = $msg
$objNotifyIcon.BalloonTipTitle = $name
 
$objNotifyIcon.Visible = $True 
$objNotifyIcon.ShowBalloonTip(10000)