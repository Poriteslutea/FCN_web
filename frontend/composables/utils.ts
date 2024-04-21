export function encodeURL(data: any) {
    
    let formBody = []
    for (var property in data) {
        var encodedKey = encodeURIComponent(property)
        var encodedValue = encodeURIComponent(data[property])
        formBody.push(encodedKey + "=" + encodedValue)
    }

    return formBody.join("&")
}