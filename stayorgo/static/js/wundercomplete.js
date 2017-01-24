/**
 * Created on 24/01/2017.
 */

// $(document).ready(function(){
//     // Constructs the suggestion engine
//     var towns = new Bloodhound({
//         datumTokenizer: Bloodhound.tokenizers.whitespace,
//         queryTokenizer: Bloodhound.tokenizers.whitespace,
//         // The url points to a json file that contains an array of country names
//         prefetch: '../data/countries.json'
//     });
//
//     // Initializing the typeahead with remote dataset
//     $('.typeahead').typeahead(null, {
//         name: 'countries',
//         source: countries,
//         limit: 10 /* Specify maximum number of suggestions to be displayed */
//     });
// });

$(load_autocomplete());

function load_autocomplete(){
    //window.query_cache = {};
    var url = 'http://autocomplete.wunderground.com/aq?format=JSON&c=AU&query=';
    var query_str;
    $('#weather_town').keyup(function(event){
        //alert('#weather_town changed: ' + data.val());
        console.log($(this).val());
        query_str = $('#weather_town').val();
        $.ajax({
            url: url + query_str,
            dataType: 'jsonp',
            jsonp: 'cb',
            success: function(data){
                console.log(data);
                $.each(data['RESULTS'],function (i, town) {
                    console.log(town.name, town.ll);
                });
            }
        });

    });

}