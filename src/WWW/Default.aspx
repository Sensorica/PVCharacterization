<%@ Page Language="C#" %>
<%@ Import Namespace="Duinocom" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html>
<head runat="server">
	<title>Default</title>
	<script runat="server">
	string portName = "";
	void Page_Load(object sender, EventArgs e)
	{
		var portDetector = new DuinoPortDetector("PVC");
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
  			$("#cameraContainer").html("<iframe src='http://127.0.0.1:8081/' frameborder='0' height='400' width='700' />");
		});

		$("#goButton").click(function() {
			$('#outputContainer').html("Loading.... (please wait)");

			var xPosition = $("#xPosition").val();
			var yPosition = $("#yPosition").val();
			var portName = $("#portName").val();
			var readCount = $("#readCount").val();

			var arguments = '?c=G&x=' + xPosition + '&y=' + yPosition + '&r=' + readCount + '&p=' + encodeURIComponent(portName);

			var sendUrl = "Send.aspx" + arguments;

			// Used for debugging
			//alert(sendUrl);

			$.ajax({
			   url:sendUrl,
			   type:'GET',
			   success: function(data){
			       $('#outputContainer').html($(data).find('#OutputContainer').html());
			   }
			});

  			//$.get( sendUrl, function( data ) {
 			// $( ".result" ).html( data );
  				//alert( "Load was performed." );
			//});
		});

		$("#xDownButton").click(function() {
			var xPosition = $("#xPosition").val();
			if (xPosition > 0)
				xPosition--;
			$("#xPosition").val(xPosition);
		});

		$("#xUpButton").click(function() {
			var xPosition = $("#xPosition").val();
			if (xPosition < 80)
				xPosition++;
			$("#xPosition").val(xPosition);
		});

		$("#yDownButton").click(function() {
			var yPosition = $("#yPosition").val();
			if (yPosition > 0)
				yPosition--;
			$("#yPosition").val(yPosition);
		});

		$("#yUpButton").click(function() {
			var yPosition = $("#yPosition").val();
			if (yPosition < 80)
				yPosition++;
			$("#yPosition").val(yPosition);
		});

		$("#xResetButton").click(function() {
			$("#xPosition").val(0);
		});

		$("#yResetButton").click(function() {
			$("#yPosition").val(0);
		});
	});
	</script>
	<form id="form1" runat="server">
	<div style="float:right">
	<div id="cameraContainer">Click "start camera"...</div>
	<input type="button" value="Start Camera" id="startCameraButton" />
	</div>
	<h1>PV Characterization</h1>
	<div>
	Port: <input type="text" name="portName" id="portName" value='<%= portName %>'/> [If not automatically detected; ensure the arduino is connected via USB and hit refresh]
	</div>
	<div>
	X: <input type="text" name="xPosition" id="xPosition" value="0"/><input type="button" id="xDownButton" value="&lt;"><input type="button" id="xUpButton" value="&gt;"><input type="button" id="xResetButton" value="Reset"> <br/>
	Y: <input type="text" name="yPosition" id="yPosition" value="0"/><input type="button" id="yDownButton" value="&lt;"><input type="button" id="yUpButton" value="&gt;"><input type="button" id="yResetButton" value="Reset"></br>
	Read count: <input type="text" name="readCount" id="readCount" value="5"/>
	<input type="button" id="goButton" value="Go" />
	</div>
	<h2>Output</h2>
	<div id="outputContainer">[Use the "Go" button above to see the output]</div>
	</form>
</body>
</html>

