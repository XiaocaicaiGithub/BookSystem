let ConstructionButton = document.querySelector('Html Body Main Button');
let ConstructionMassages = document.querySelectorAll('Html Body Main Span');
let ConstructionInputs = document.querySelectorAll('Html Body Main Label Input');

function Construction() {
    let ConstructionName = ConstructionInputs[0].value;
    let ConstructionCode = ConstructionInputs[1].value;
    let ConstructionInfo = ConstructionInputs[2].value;
    let ConstructionPrice = ConstructionInputs[3].value;
    if (!ConstructionName) {
        ConstructionMassages[1].textContent = '书名不能为空！';
    } else if (!ConstructionCode) {
        ConstructionMassages[1].textContent = '';
        ConstructionMassages[2].textContent = '书本代码不能为空！';
    } else {
        function ConstructionResponse() {
            if (ConstructionRequest.status === 200) {
                let ConstructionResponse = ConstructionRequest.responseText;
                if (ConstructionResponse === 'Success') {
                    location.assign('/Books')
                } else {
                    ConstructionMassages[0].textContent = ConstructionResponse;
                    ConstructionMassages[1].textContent = '';
                    ConstructionMassages[2].textContent = '';
                }
            } else {
                ConstructionMassages[0].textContent = '添加书本失败！'
            }
        }

        let ConstructionRequest = new XMLHttpRequest();
        ConstructionRequest.open('POST', '/Book/Construction', true);
        ConstructionRequest.setRequestHeader('Content-Type', 'application/json')
        ConstructionRequest.send(JSON.stringify({
            'Info': ConstructionInfo,
            'Name': ConstructionName,
            'Code': ConstructionCode,
            'Price': ConstructionPrice
        }))
        ConstructionRequest.onreadystatechange = ConstructionResponse;
    }
}

ConstructionButton.onclick = Construction;
