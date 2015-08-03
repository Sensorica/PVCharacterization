<%@ Page Language="C#" %>
<%@ Import Namespace="PVC.Core" %>
<!DOCTYPE html>
<html>
<head runat="server">
	<title>Send</title>
	<script runat="server">
	void Page_Load(object sender, EventArgs e)
	{

		var commandSender = new CommandSender();

		var commandLetter = Request.QueryString["c"];

		if (commandLetter == "G")
		{
			var xPosition = Convert.ToInt32(Request.QueryString["x"]);
			var yPosition = Convert.ToInt32(Request.QueryString["y"]);

			if (Session["XPosition"] == null)
				Session["XPosition"] = 0;
			if (Session["YPosition"] == null)
				Session["YPosition"] = 0;

			if (Session["XPosition"].ToString() != xPosition.ToString())
			{
				commandSender.Send("GX" + xPosition);
				Session["XPosition"] = xPosition;
			}

			if (Session["YPosition"].ToString() != xPosition.ToString())
			{
				Session["YPosition"] = yPosition;
				commandSender.Send("GY" + yPosition);
			}
		}
	}
	</script>
</head>
<body>
	<form id="form1" runat="server">
	
	</form>
</body>
</html>

