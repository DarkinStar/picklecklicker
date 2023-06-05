$(document).ready(function () {
    function getTotalCount() {
        $.ajax({
            type: 'GET',
            url: '/backend/get/',
            success: function (response) {
                $('#total-count').text(response.total_count);
                $('#inc-value').text(response.inc_value);
                $('#click_per_sec').text(response.click_per_sec);
                $('#ppc-cost').text(response.click_boost_inc_cost);
                $('#pps-cost').text(response.click_per_sec_inc_cost);
            }
        });
    }
    getTotalCount();
});
function incrementTotalCount() {
    $.ajax({
        type: 'POST',
        url: '/backend/increase/',
        success: function (response) {
            $('#total-count').text(response.total_count);
            $('#inc-value').text(response.inc_value);
            $('#ppc-cost').text(response.click_boost_inc_cost);
            $('#pps-cost').text(response.click_per_sec_inc_cost);
        }
    });
}

function incrementBoost() {
    $.ajax({
        type: 'POST',
        url: '/backend/increase_boost/',
        success: function (response) {
            $('#total-count').text(response.total_count);
            $('#inc-value').text(response.inc_value);
            $('#ppc-cost').text(response.click_boost_inc_cost);
            $('#pps-cost').text(response.click_per_sec_inc_cost);
        }
    });
}

function logout() {
    $.ajax({
        type: 'GET',
        url: '/backend/logout/',
        success: function (response) {
            location.replace("");
        }
    });
}
$('#logout').click(function () {
    $.ajax({
        type: 'POST',
        url: '/backend/logout/',
        success: function (response) {
            location.replace("");
        }
    });
});

function pickleclick() {
    document.getElementById("pickle").style.left = Math.floor(Math.random() * 1200).toString() + "px";
    document.getElementById("pickle").style.top = Math.floor(Math.random() * 600).toString() + "px";
    incrementTotalCount()
};

function buyAutoClick() {
    $.ajax({
        type: 'POST',
        url: '/backend/buy_auto_click/',
        success: function (response) {
            $('#total-count').text(response.total_count);
            $('#click_per_sec').text(response.click_per_sec);
            $('#ppc-cost').text(response.click_boost_inc_cost);
            $('#pps-cost').text(response.click_per_sec_inc_cost);
        }
    });
}

setInterval(
    function autoIncease() {
        var rate = parseInt(document.getElementById("click_per_sec").innerText);
        if (rate > 0) {
            $.ajax({
                type: 'POST',
                url: '/backend/auto_increase/',
                dataType: "json",
                success: function (response) {
                    $('#total-count').text(response.total_count);
                    $('#click_per_sec').text(response.click_per_sec);
                }
            });
        }
    },
    1000
);
