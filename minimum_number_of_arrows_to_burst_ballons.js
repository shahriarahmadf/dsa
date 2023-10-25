/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    const sortedPoints = points.sort((a,b) => a[0] - b[0]);
    console.log(sortedPoints);
    
    const commonIntervalFinder = (point1, point2) => {
        const lowerLimit = Math.max(point1[0],point2[0]);
        const higherLimit = Math.min(point1[1],point2[1]);
        return [lowerLimit,higherLimit];
    };

    let commonInterval = sortedPoints[0];
    let arrow = 1;
    for (let i=1; i<sortedPoints.length; i++){
        if (sortedPoints[i][0] <= commonInterval[1]){
            commonInterval = commonIntervalFinder(commonInterval, sortedPoints[i]);
        }else{
            arrow++;
            commonInterval = sortedPoints[i];
        }
    }    
    return arrow;
};