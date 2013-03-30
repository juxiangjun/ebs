//股票档案
function showProfile() {
    url = "/stock/getProfile";
    form = $("#frmQuery").serialize();
    $.post(url, form, function(html) {
        $("#stock_contents").html(html);
    }); 
}
//财务指标
function showFinanceIndex() {
    url = "/stock/getFinanceIndex";
    form = $("#frmQuery").serialize();
    $.post(url, form, function(html) {
        $("#stock_contents").html(html);
    }); 
}
//报表主要指标预测
function showFinancePrediction() {
    url = "/stock/getFinancePrediction";
    form = $("#frmQuery").serialize();
    $.post(url, form, function(html) {
        $("#stock_contents").html(html);
    }); 
}
//指标排名
function showFinanceIndexRank() {
    url = "/stock/getFinanceIndexRank";
    form = $("#frmQuery").serialize();
    $.post(url, form, function(html) {
        $("#stock_contents").html(html);
    }); 
}
