window.addEventListener('load', () => {
	const canvas = document.querySelector("#myCanvas");
	const ctx = canvas.getContext("2d");

	// Resize
	canvas.height = window.innerHeight;
	canvas.width = window.innerWidth;

	// necessary variables
	var drawing = false;

	// functions
	function startPosition(e){
		drawing = true;
		draw(e);
	}
	function endPosition(){
		drawing = false;
		ctx.beginPath();
	}
	function draw(e){
		if(!drawing) return;
		ctx.lineWidth = 10;
		ctx.lineCap = "round";

		ctx.lineTo(e.clientX, e.clientY);
		ctx.stroke();
		ctx.beginPath();
		ctx.moveTo(e.clientX, e.clientY);

	}

	// even listeneres
	canvas.addEventListener("mousedown", startPosition);
	canvas.addEventListener("mouseup", endPosition);
	canvas.addEventListener("mousemove", draw);
});