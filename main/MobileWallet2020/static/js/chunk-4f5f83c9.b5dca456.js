(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4f5f83c9"],{"3a07":function(t,e,n){},a026:function(t,e,n){"use strict";var a=n("3a07"),o=n.n(a);o.a},a55b:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{"pure-form":"","pure-form-aligned":""}},[n("h2",[t._v("Login")]),n("input",{directives:[{name:"model",rawName:"v-model",value:t.input.username,expression:"input.username"}],attrs:{type:"text",name:"username",placeholder:"Username"},domProps:{value:t.input.username},on:{input:function(e){e.target.composing||t.$set(t.input,"username",e.target.value)}}}),n("input",{directives:[{name:"model",rawName:"v-model",value:t.input.password,expression:"input.password"}],attrs:{type:"password",name:"password",placeholder:"Password"},domProps:{value:t.input.password},on:{input:function(e){e.target.composing||t.$set(t.input,"password",e.target.value)}}}),n("button",{staticClass:"pure-button pure-button-primary",attrs:{type:"button"},on:{click:function(e){return t.nam_test()}}},[t._v("Login")])])},o=[],s=n("d697"),r={name:"Login",props:{msg:String},data:function(){return{input:{username:""}}},mounted:function(){},methods:{nam_test:function(){var t=this;""==this.input.username||""==this.input.password?alert("Please provide Username and Password"):this.axios.post(s["a"]+"auth-tokens",{username:this.input.username,password:this.input.password}).then((function(e){console.log(e),t.$emit("authenticated",!0),localStorage.setItem("auth-token",e.data.token);var n=localStorage.getItem("auth-token");t.axios.defaults.headers.common["Authorization"]="Token "+n,t.$router.push({name:"customer-info"})})).catch((function(e){console.log(e),alert("Cannot login with your credentials, please try again."),t.input.username="",t.input.password=""}))}},components:{}},u=r,i=(n("a026"),n("2877")),p=Object(i["a"])(u,a,o,!1,null,"fd91fb18",null);e["default"]=p.exports},d697:function(t,e,n){"use strict";n.d(e,"a",(function(){return a}));var a="/api/v1/"}}]);
//# sourceMappingURL=chunk-4f5f83c9.b5dca456.js.map