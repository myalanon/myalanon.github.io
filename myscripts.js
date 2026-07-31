


// <div id="demo" style="white-space: pre-wrap;"></div>
// '\u00A9' is copyribht char
// document.getElementById("demo").innerHTML=


function ctacold() 
{
//   MYAT = '@';
//    MYNEXT1 = 'i';
//    MYPD='.';
//    MYNEXT2='c';
//    zz= 'mailto:' + String.fromCharCode(parseInt(0x49, 16))+'f'+'a'+'l'+'a'+'n'+'o'+'n'+ MYAT +'g'+'m'+'a'+ MYNEXT1+'l'+ MYPD + MYNEXT2 +'o'+'m';
    zzz = "mailto:steve@example.com";
    window.location.href = zzz;
}


function ctac() {
    const mailtoUrl = "mailto:sfalanon@gmail.com";
    
    const link = document.createElement('a');
    link.href = mailtoUrl;
    link.style.display = 'none';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link); // Clean up the DOM
}