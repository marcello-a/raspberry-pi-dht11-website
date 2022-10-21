// gridlines in x axis function
function make_x_gridlines(x) {		
    return d3.axisBottom(x)
        .ticks(5)
}

// gridlines in y axis function
function make_y_gridlines(y) {		
    return d3.axisLeft(y)
        .ticks(5)
}




function addGrid(width, height, svg) {

    // set the ranges
    var x = d3.scaleTime().range([0, width]);
    var y = d3.scaleLinear().range([height, 0]);

    // // add the X gridlines
    // svg.append("g")			
    // .attr("class", "grid")
    // .attr("transform", "translate(0," + height + ")")
    // .call(make_x_gridlines(x)
    //     .tickSize(-height)
    //     .tickFormat("")
    // )

    // add the Y gridlines
    svg.append("g")			
    .attr("class", "grid")
    .call(make_y_gridlines(y)
        .tickSize(-width)
        .tickFormat("")
    )
}

