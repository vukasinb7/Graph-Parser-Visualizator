let observer= new MutationObserver(function(mutations,observer){
    //copy content from main canvas to birdview
    d3.select("#canvas-birdview g#main").html(d3.select("#canvas-simple g").html());

    let canvasNode=d3.select('#canvas-simple g').node();
    let canvasWidth=canvasNode.getBBox().width;
    let canvasHeight=canvasNode.getBBox().height;
    let canvasBirdviewGNode=d3.select("#canvas-birdview g#main").node();
    let birdWidth=document.getElementById("canvas-birdview").clientWidth;
    let birdHeight=document.getElementById("canvas-birdview").clientHeight;
    let finalScale=birdHeight/canvasHeight;
    if ((birdWidth/canvasWidth)<(birdHeight/canvasHeight)) {
        finalScale = birdWidth / canvasWidth;
    }
    let translate=[-canvasBirdviewGNode.getBBox().x*finalScale,
        -canvasBirdviewGNode.getBBox().y*finalScale];
    d3.select("#canvas-birdview g#main")
        .attr("transform", "translate(" + translate + ")" + " scale(" + finalScale + ")");



});
observer.observe( d3.select("#canvas-simple").node(),{subtree:true, attributes:true});