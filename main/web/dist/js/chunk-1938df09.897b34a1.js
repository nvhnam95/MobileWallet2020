(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-1938df09"],{"7a40":function(t,a,n){"use strict";var e=n("a82c"),o=n.n(e);o.a},"8f0c":function(t,a,n){"use strict";n.r(a);var e=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("div",[n("div",{staticClass:"account-info"},[n("h1",[t._v("Customer Info")]),n("p",[t._v("Hello "+t._s(t.username))]),n("p",[t._v("Your balance is "),n("b",[t._v(t._s(t.balance))]),t._v(" SGD")]),n("p",[t._v("You have "+t._s(t.number_of_saving_account)+" saving account(s), with "+t._s(t.total_interest)+" SGD of interest until now.")]),n("router-link",{staticClass:"nav-link",attrs:{to:{name:"create-saving-account"},"active-class":"active"}},[t._v("Create a new saving account?")]),t._v(" "),n("br"),n("router-link",{staticClass:"nav-link",attrs:{to:{name:"delete-saving-account"},"active-class":"active"}},[t._v("Delete a saving account and get the interest.")])],1),n("div",[n("p",[n("router-link",{staticClass:"nav-link",attrs:{to:{name:"transfer-money"},"active-class":"active"}},[t._v("Tranfer money")])],1),n("p",[n("router-link",{staticClass:"nav-link",attrs:{to:{name:"deposit"},"active-class":"active"}},[t._v("Deposit")])],1)]),n("br"),n("br"),n("div",{staticClass:"functions"},[n("h1",[t._v(" Transaction history ")]),n("TransactionTable")],1)])},o=[],s=n("d697"),c=function(){var t=this,a=t.$createElement,n=t._self._c||a;return n("v2-table",{attrs:{data:t.data}},[n("v2-table-column",{attrs:{label:"Transaction ID",prop:"id"}}),n("v2-table-column",{attrs:{label:"Sender",prop:"sender"}}),n("v2-table-column",{attrs:{label:"Receiver",prop:"receiver"}}),n("v2-table-column",{attrs:{label:"Amount",prop:"amount"}}),n("v2-table-column",{attrs:{label:"Time",prop:"created_time"}})],1)},i=[],r={data:function(){return{data:[]}},mounted:function(){var t=this;this.axios.get("http://localhost/api/v1/transactions").then((function(a){console.log(a),t.data=a.data})).catch((function(t){console.log(t)}))}},l=r,u=n("2877"),v=Object(u["a"])(l,c,i,!1,null,null,null),m=v.exports,_={name:"Register",props:{msg:String},mounted:function(){var t=this;this.axios.get(s["a"]+"customers/info").then((function(a){console.log(a),t.balance=a.data.balance,t.username=a.data.username})).catch((function(a){console.log(a),localStorage.removeItem("auth-token"),t.$router.push({name:"login"})})),this.axios.get(s["a"]+"saving-accounts").then((function(a){t.number_of_saving_account=a.data.length;for(var n=0;n<t.number_of_saving_account;n++)t.total_interest+=a.data[n].interest})).catch((function(a){console.log(a),t.$router.push({name:"login"})}))},data:function(){return{balance:0,username:"",number_of_saving_account:0,total_interest:0}},components:{TransactionTable:m}},f=_,p=(n("7a40"),Object(u["a"])(f,e,o,!1,null,"2032375e",null));a["default"]=p.exports},a82c:function(t,a,n){},d697:function(t,a,n){"use strict";n.d(a,"a",(function(){return e}));var e=":8080/api/v1/"}}]);
//# sourceMappingURL=chunk-1938df09.897b34a1.js.map