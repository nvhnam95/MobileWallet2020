(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-8cdefb5e"],{"5bf2":function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("p",[e._v("Your Balance is "+e._s(e.balance)+" SGD")]),n("input",{directives:[{name:"model",rawName:"v-model",value:e.amount,expression:"amount"}],attrs:{type:"text",name:"amount",placeholder:"How much do you want to save?"},domProps:{value:e.amount},on:{input:function(t){t.target.composing||(e.amount=t.target.value)}}}),n("p",[e._v("Saving type:")]),n("select",{directives:[{name:"model",rawName:"v-model",value:e.saving_type,expression:"saving_type"}],on:{change:function(t){var n=Array.prototype.filter.call(t.target.options,(function(e){return e.selected})).map((function(e){var t="_value"in e?e._value:e.value;return t}));e.saving_type=t.target.multiple?n:n[0]}}},e._l(e.saving_types,(function(t){return n("option",{key:t,domProps:{value:t}},[e._v(e._s(t))])})),0),n("br"),n("br"),n("button",{attrs:{type:"button"},on:{click:function(t){return e.deposit()}}},[e._v("Create")]),n("p",[n("router-link",{staticClass:"nav-link",attrs:{to:{name:"customer-info"},"active-class":"active"}},[e._v("Back")])],1)])},o=[],r=n("d697"),i={name:"CreateSavingAccount",props:{msg:String},mounted:function(){var e=this;this.axios.get(r["a"]+"customers/info").then((function(t){console.log(t),e.balance=t.data.balance,e.username=t.data.username})).catch((function(t){console.log(t),localStorage.removeItem("auth-token"),e.$router.push({name:"login"})}))},data:function(){return{balance:0,amount:0,saving_type:"",saving_types:["yearly","quarterly","monthly","every_minute"]}},components:{},methods:{deposit:function(){var e=this;""==this.amount?alert("Please provide amount"):this.axios.post(r["a"]+"saving-accounts",{balance:this.amount,saving_type:this.saving_type}).then((function(t){console.log(t),alert("Created, thank you!"),e.$router.push({name:"customer-info"})})).catch((function(e){console.log(e),alert("There are an error happened, please try again later")}))}}},s=i,u=(n("bdb2"),n("2877")),c=Object(u["a"])(s,a,o,!1,null,"0e5eef24",null);t["default"]=c.exports},a45f:function(e,t,n){},bdb2:function(e,t,n){"use strict";var a=n("a45f"),o=n.n(a);o.a},d697:function(e,t,n){"use strict";n.d(t,"a",(function(){return a}));var a="/api/v1/"}}]);
//# sourceMappingURL=chunk-8cdefb5e.24cb5ff8.js.map