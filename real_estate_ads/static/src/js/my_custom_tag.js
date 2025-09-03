odoo.define('real_estate_ads.CustmonAction',function(require){
    "use strict";
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var CustmonAction = AbstractAction.extend({
            template : "CustomActions",
            start: function(){
            console.log("Action")
            }
    })
    core.action_registry.add("custom_client_action",CustomAction)
});
