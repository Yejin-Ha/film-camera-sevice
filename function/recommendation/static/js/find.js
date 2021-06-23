function findcam() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            // data = JSON.parse(this.responseText);
            data = this.responseText;
            console.log('hi')

            tab = `
            <table border="1">
                <tr><th>브랜드</th><th>모델명</th><th>가격</th><th>카테고리</th><th>셔터</th><th>노출측정방식</th><th>레벨</th><th>이미지</th></tr>`;

            for (no in data) {
                console.log('hi123123')
                tab = tab + `<tr>
                    <td><img src="../../../project/img/camera_image/${data[no].brand}_${data[no].model}.jpg"></td>
                    <td>${data[no].brand}</td>
                    <td>${data[no].model}</td>
                    <td>${data[no].price}</td>
                    <td>${data[no].category}</td>
                    <td>${data[no].shutter}</td>
                    <td>${data[no].exposure}</td>
                    <td>${data[no].test_level}</td>
                </tr>`;
                console.log(brand + "_" + model)
            }
            tab = tab + `</table>`;
            document.getElementById("demo").innerHTML = tab;
        };
    };
    xhttp.open("POST", "camfind");
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("test_level=" + document.getElementById("newTest_level").value);
}
