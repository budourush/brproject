//innerHTML, textContent
document.addEventListener('DOMContentLoaded', function(){
    //配下の要素を置き換え=textContent
    document.getElementById('result_text').textContent =
    '<a href="https://ainow.ai/">ai now</a>';
    //HTMLとしてテキストに埋め込み
    document.getElementById('result_html').innerHTML =
    '<a href="https://ainow.ai/">ai now</a>';
}, false);

//入力ボックスの値を取得
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('btn').addEventListener('click', function(){
        var name = document.getElementById('name');
        console.log(name.value);
    }, false)
}, false);

//チェックボックスの値を取得
document.addEventListener('DOMContentLoaded', function(){
    //ボタンクリック時にダイアログ表示
    document.getElementById('btn2').addEventListener('click', function(){
        //選択値を格納するための配列
        var result = [];
        var foods = document.getElementsByName('food');
        //チェックボックスの状態を確認する
        for (var i = 0, len = foods.length; i < len; i++){
            var food = foods.item(i);
            if (food.checked){
                result.push(food.value);
            }
        }
        //配列の内容をダイアログ表示
        window.alert(result.toString());
    }, false)
}, false);