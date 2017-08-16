// Wrap strong tag / 強調タグで囲む
$('#wrap-strong').click(function(){
  $('#textarea')
    // insert before string '<strong>'
    // <strong> を選択テキストの前に挿入
    .selection('insert', {text: '<strong>', mode: 'before'})
    // insert after string '</strong>'
    // </strong> を選択テキストの後に挿入
    .selection('insert', {text: '</strong>', mode: 'after'});
});

// Wrap link tag / リンクタグで囲む
$('#wrap-link').click(function(){
  // Get selected text / 選択テキストを取得
  var selText = $('#textarea').selection();

  $('#textarea')
    // insert before string '<a href="'
    // <a href=" を選択テキストの前に挿入
    .selection('insert', {text: '<a href="', mode: 'before'})
    // replace selected text by string 'http://'
    // 選択テキストを http:// に置き換える（http:// を選択状態に）
    .selection('replace', {text: 'http://'})
    // insert after string '">SELECTED TEXT</a>' 
    // ">選択テキスト</a> を選択テキストの後に挿入
    .selection('insert', {text: '">'+ selText + '</a>', mode: 'after'});
});

// Get selected text / 選択テキストを取得
$('#sel-textarea').click(function(){
  // alert selected text
  // テキストエリアの選択範囲をアラートする
  alert($('#textarea').selection());
  $('#textarea').focus();
});