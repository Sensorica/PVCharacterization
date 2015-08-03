<%@ Page Language="C#" %>
<%@ Import Namespace="Duinocom" %>
<!DOCTYPE html>
<html>
<head runat="server">
	<title>Send</title>
	<script runat="server">
	void Page_Load(object sender, EventArgs e)
	{
		var portName = Request.QueryString["p"];

		var communicator = new DuinoCommunicator(portName);

		var commandLetter = Request.QueryString["c"];

		if (commandLetter == "G")
		{
			var xPosition = Convert.ToInt32(Request.QueryString["x"]);
			var yPosition = Convert.ToInt32(Request.QueryString["y"]);
			var readCount = Convert.ToInt32(Request.QueryString["r"]);

			if (Session["XPosition"] == null)
				Session["XPosition"] = 0;
			if (Session["YPosition"] == null)
				Session["YPosition"] = 0;

			//if (Convert.ToInt32(Session["XPosition"]) != xPosition)
			//{
				var xResult = communicator.Send("GX" + xPosition);
				Output(xResult);
				Session["XPosition"] = xPosition;
			//}

			//if (Convert.ToInt32(Session["YPosition"]) != xPosition)
			//{
				Session["YPosition"] = yPosition;
				var yResult = communicator.Send("GY" + yPosition);
				Output(yResult);
			//}

			var readResult = communicator.Send("R" + readCount);

			Output(readResult);
		}
	}

	void Output(string result)
	{
		OutputContainer.Controls.Add(new LiteralControl("<div>" + result.Replace(Environment.NewLine, "<br/>") + "</div>"));
	}
	</script>
</head>
<body>
	<form id="form1" runat="server">
		<asp:Panel runat="server" id="OutputContainer"/>
	</form>
</body>
</html>

