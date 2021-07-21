var xmlhttp = new XMLHttpRequest();
var url = "/static/index/json/hyundai/hyundai_car2021_01~_project.json";
xmlhttp.open("GET", url, true);
xmlhttp.send();
xmlhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
        var data = JSON.parse(this.responseText);
        //console.log(data);
        var predDate = data.data.map(function(elem){
            elem.pred_date=elem.pred_date.substr(0, 10)
            return elem.pred_date;
        });
        //console.log(predictPrice)
        var predictPrice = data.data.map(function(elem){
            return elem.pred_close;
        });
        var realPrice = data.data.map(function(elem){
            return elem.target_close ;
        });
        var closePrice = data.data.map(function(elem){
            return elem.Close;
        });


        var ctx = document.getElementById('hd_canvas_04').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: predDate,
        datasets: [{
            label: 'predictPrice',
            data: predictPrice,
            backgroundColor: 'transparent',
            pointStyle: 'cross',
            borderColor: 'rgb(255, 99, 132)',
            borderWidth: 1
        },
        {
            label: 'realPrice',
            data: realPrice,
            backgroundColor: 'transparent',
            pointStyle: 'cross',
            borderColor: 'rgb(54, 162, 235)',
            borderWidth: 1
        },
        {
            label: 'closePrice',
            data: closePrice,
            backgroundColor: 'transparent',
            pointStyle: 'cross',
            borderColor: 'red',
            borderWidth: 1
        }]
    },
    options: {
        elements:{
            line:{
                tension:0
            }
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
    }
}

