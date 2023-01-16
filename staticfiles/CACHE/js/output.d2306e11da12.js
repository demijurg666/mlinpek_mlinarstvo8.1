function updateCart(){let updateBtns=document.getElementsByClassName('update-cart')
for(let i=0;i<updateBtns.length;i++){updateBtns[i].addEventListener('click',function(){let productId=this.dataset.product
let action=this.dataset.action
console.log('productId:',productId,'action:',action)
console.log('USER:',user)
if(user=='AnonymousUser'){console.log('User is not authenticated')}else{updateUserOrder(productId,action)}})}}
function updateUserOrder(productId,action){console.log('user is authenticated, sending data.. ')
let url='/update_item/';fetch(url,{method:'POST',headers:{'Content-Type':'application/json','X-CSRFToken':csrftoken,},body:JSON.stringify({'productId':productId,'action':action})}).then((response)=>{return response.json()}).then((data)=>{console.log('data:',data)
location.reload()});};let user="Korisnik1";function getToken(name){let cookieValue=null;if(document.cookie&&document.cookie!==""){let cookies=document.cookie.split(";");for(let i=0;i<cookies.length;i++){let cookie=cookies[i].trim();if(cookie.substring(0,name.length+1)===name+"="){cookieValue=decodeURIComponent(cookie.substring(name.length+1));break;}}}
return cookieValue;}
let csrftoken=getToken("csrftoken");;