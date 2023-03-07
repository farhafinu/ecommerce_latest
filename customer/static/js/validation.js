function c_validation(){

    var address = document.getElementById('c_address').value
    var email = document.getElementById('c_mail').value
    var password = document.getElementById('c_pass').value
    var email_pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
    var password_pattern = "/^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{7,}$/"

    if (address == ''){
        document.getElementById('c_add').innerHTML ='Please fill out this field' /*span id c_add */
        document.getElementById('c_address').style.borderBottom='1px solid red'
        document.getElementById('c_add').style.color ='red'

    }
    else{
        document.getElementById('c_add').innerHTML =''
    }
    if (email == ''){
       
        document.getElementById('mail_c').innerHTML ='Please fill out this field'/*span id mail_c */
        document.getElementById('c_mail').style.borderBottom='1px solid red'
        document.getElementById('mail_c').style.color ='red'
        
    }
    else{
        document.getElementById('mail_c').innerHTML =''
        document.getElementById('c_mail').style.color ='blue 1px solid'
        if (email_pattern == null()){
            document.getElementById('mail_c').innerHTML ='email pattern incorrect'/*check */
        }
    }
    if (password == ''){
        
        document.getElementById('c_pswd').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('c_pass').style.borderBottom ='red 1px solid'
        document.getElementById('c_pswd').style.color ='red'
        
    }
    else{
        document.getElementById('c_pswd').innerHTML =''
        document.getElementById('c_pass').style.color ='blue 1px solid'
    }
}

function s_validation(){
    var name = document.getElementById('i_s_name').value
    var address = document.getElementById('i_s_address').value
    var email = document.getElementById('i_s_email').value
    var password = document.getElementById('i_s_pwd').value
    var acname = document.getElementById('i_s_acname').value
    var acno = document.getElementById('i_s_acno').value
    var ifsc = document.getElementById('i_s_ifsc').value

    var email_pattern = "[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$"
    var password_pattern = "/^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z0-9]{7,}$/"

    if (address == ''){
        document.getElementById('s_s_address').innerHTML ='Please fill out this field' /*span id c_add */
        document.getElementById('i_s_address').style.borderBottom='1px solid red'
        document.getElementById('s_s_address').style.color ='red'

    }
    else{
        document.getElementById('s_s_address').innerHTML =''
        document.getElementById('i_s_address').style.color ='blue 1px solid'
    }
    if (email == ''){
       
        document.getElementById('s_s_email').innerHTML ='Please fill out this field'/*span id mail_c */
        document.getElementById('i_s_email').style.borderBottom='1px solid red'
        document.getElementById('s_s_email').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_email').innerHTML =''
        document.getElementById('i_s_email').style.color ='blue 1px solid'
        if (email_pattern == null()){
            document.getElementById('s_s_email').innerHTML ='email pattern incorrect'/*check */
        }
    }
    if (password == ''){
        
        document.getElementById('s_s_pwd').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('i_s_pwd').style.borderBottom ='red 1px solid'
        document.getElementById('s_s_email').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_pwd').innerHTML =''
        document.getElementById('i_s_pwd').style.color ='blue 1px solid'
    }
    if (name == ''){
        
        document.getElementById('s_s_name').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('i_s_name').style.borderBottom ='red 1px solid'
        document.getElementById('s_s_name').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_name').innerHTML =''
        document.getElementById('i_s_name').style.color ='blue 1px solid'
    }
    if (acname == ''){
        
        document.getElementById('s_s_acname').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('i_s_acname').style.borderBottom ='red 1px solid'
        document.getElementById('s_s_acname').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_acname').innerHTML =''
        document.getElementById('i_s_acname').style.color ='blue 1px solid'
    }
    if (acno == ''){
        
        document.getElementById('s_s_acno').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('i_s_acno').style.borderBottom ='red 1px solid'
        document.getElementById('s_s_acno').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_acno').innerHTML =''
        document.getElementById('i_s_acno').style.color ='blue 1px solid'
    }
    if (ifsc == ''){
        
        document.getElementById('s_s_ifsc').innerHTML ='Please fill out this field'/*span id c_pswd*/
        document.getElementById('i_s_ifsc').style.borderBottom ='red 1px solid'
        document.getElementById('s_s_ifsc').style.color ='red'
        
    }
    else{
        document.getElementById('s_s_ifsc').innerHTML =''
        document.getElementById('i_s_ifsc').style.color ='blue 1px solid'
    }

}