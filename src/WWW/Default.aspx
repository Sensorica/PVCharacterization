<%@ Page Language="C#" %>
<%@ Import Namespace="PVC.Core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
<head runat="server">
	<title>Default</title>
	<script runat="server">
	string portName = "";
	void Page_Load(object sender, EventArgs e)
	{
		var portDetector = new SerialPortDetector();
		portName = portDetector.Detect();
		if (String.IsNullOrEmpty(portName))
			portName = "[unable to detect]";
	}
	</script>
	<style>
		body
		{
			font-family: Verdana;
			font-size: 11px;
		}

		div
		{
		padding: 4px;
		}
	</style>
</head>
<body>
	<script language="javascript" type="text/javascript" src="jquery-2.1.3.min.js"></script>
	<script>

	$(document).ready(function(){
		$("#startCameraButton").click(function() {
  			$("#cameraContainer").html("<iframe src='http://127.0.0.1:8081/' />");
		});

		$("#goButton").click(function() {
			var xPosition = $("#xPosition").val();
			var yPosition = $("#yPosition").val();
			var portName = $("#portName").val();

			var arguments = '?c=G&x=' + xPosition + '&y=' + yPosition + '&p=' + encodeURIComponent(portName);
			alert(arguments);
  			$.get( "Send.aspx" + arguments, function( data ) {
 			 $( ".result" ).html( data );
  				//alert( "Load was performed." );
			});
		});
	});
	</script>
	<form id="form1" runat="server">
	<h1>PV Characterization</h1>
	<div>
	Port: <input type="text" name="portName" id="portName" value='<%= portName %>'/>
	</div>
	<div>
	X: <input type="text" name="xPosition" id="xPosition" value="0"/> 
	Y: <input type="text" name="yPosition" id="yPosition" value="0"/> 
	<input type="button" id="goButton" value="Go" />
	</div>
	<div>
	<div id="cameraContainer">Click "start camera"...</div>
	<input type="button" value="Start Camera" id="startCameraButton" />
	</div>
	</form>
</body>
</html>

