console.log(
	"%c                      ______                           __            \n  ___________   __   / ____/__  ____  ___  _________ _/ /_____  _____\n / ___/ ___/ | / /  / / __/ _ \\/ __ \\/ _ \\/ ___/ __ `/ __/ __ \\/ ___/\n/ /__(__  )| |/ /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    \n\\___/____/ |___/   \\____/\\___/_/ /_/\\___/_/   \\__,_/\\__/\\____/_/     ",
	"color:green;"
);

var h_choice = document.querySelector(".play-page-gamer__choices");
var h_rock = document.querySelector(".play-page-gamer__choices").childNodes[1];
var h_paper = document.querySelector(".play-page-gamer__choices").childNodes[3];
var h_scissors = document.querySelector(".play-page-gamer__choices")
	.childNodes[5];

var v_choice = document.querySelectorAll(".play-page-gamer__choices")[1];
var v_rock = document.querySelectorAll(".play-page-gamer__choices")[1]
	.childNodes[6];
var v_paper = document.querySelectorAll(".play-page-gamer__choices")[1]
	.childNodes[8];
var v_scissors = document.querySelectorAll(".play-page-gamer__choices")[1]
	.childNodes[10];

var game = [];
var games = [];

h_rock.onclick = () => {
	if (
		h_paper.childNodes[2].textContent != "" &&
		h_scissors.childNodes[2].textContent != ""
	) {
		game.push("rock");
	}
};

h_paper.onclick = () => {
	if (
		h_rock.childNodes[2].textContent != "" &&
		h_scissors.childNodes[2].textContent != ""
	) {
		game.push("paper");
	}
};

h_scissors.onclick = () => {
	if (
		h_rock.childNodes[2].textContent != "" &&
		h_paper.childNodes[2].textContent != ""
	) {
		game.push("scissors");
	}
};

var V_mutationObserver = new MutationObserver(() => {
	if (v_choice.childNodes[6].tagName == "IMG") {
		game.push(v_choice.childNodes[6].src.split("/").pop().split(".")[0]);
	} else if (v_choice.childNodes[8].tagName == "IMG") {
		game.push(v_choice.childNodes[8].src.split("/").pop().split(".")[0]);
	} else if (v_choice.childNodes[10].tagName == "IMG") {
		game.push(v_choice.childNodes[10].src.split("/").pop().split(".")[0]);
	}
});

V_mutationObserver.observe(v_choice, { childList: true });

var finalScreen = new MutationObserver(() => {
	if (!!document.querySelector("button.btn-primary")) {
		console.log(game);
	}
});

finalScreen.observe(
	document.querySelector(".container > app-playing:nth-child(1)"),
	{ childList: true }
);
