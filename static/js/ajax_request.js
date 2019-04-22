function ajax_request(body, url,method, contentType = null, processData = null, stringify = false,handleData = false, failure_function = false) // = "application/json; charset=utf-8"
{



   var params = {
        async: true,
        type: "POST",
        method:"POST",
        url:  window.location.origin + url,
        data: stringify ? JSON.stringify(body): body
        }

    if (contentType !==null)
    params.contentType = contentType
    if (processData!==null)
    params.processData = processData;


    if (handleData)
    params.success = handleData;

    if (failure_function)
    params.error = failure_function;

    $.ajax(params);

}