$(document).ready(function(){

	xyz = 0
	for (i = 0; i < JsonData.length; i++) {
		console.log(JsonData[i].episodeTitle);
		$("tbody").append("<tr class='number " + (xyz++) + "'><td>" + JsonData[i].episodeTitle + "<br>" + (JsonData[i].musicData || "") + "</td></tr>")
	}

	//$("table>tbody>tr>td:first-child").css("border-radius", "20px;");
	//jQuery test $(".description-container").css("background-color", "blue");

	$(".updated-time-container").text("This table was last updated on " + timeUpdated + ".");

});