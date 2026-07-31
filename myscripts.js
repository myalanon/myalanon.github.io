

// <div id="demo" style="white-space: pre-wrap;"></div>
// '\u00A9' is copyribht char


MYAT = '@';
MYNEXT1 = 'i';
MYPD='.';
MYNEXT2='c';
document.getElementById("demo").innerHTML=
String.fromCharCode(parseInt(0x49, 16))+'f'+'a'+'l'+'a'+'n'+'o'+'n'+ MYAT +'g'+'m'+'a'+ MYNEXT1+'l'+ MYPD + MYNEXT2 +'o'+'m';
