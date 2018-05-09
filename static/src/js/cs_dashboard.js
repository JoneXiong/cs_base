odoo.define('cs_base.BaseDashboard', function (require) {
"use strict";

var core = require('web.core');
var framework = require('web.framework');
var PlannerCommon = require('web.planner.common');
var PlannerDialog = PlannerCommon.PlannerDialog;
var Widget = require('web.Widget'); 

var QWeb = core.qweb;          
var _t = core._t;

var Dashboard = Widget.extend({
	template: 'CsBaseDashboard',



});


core.action_registry.add('cs_base_dashboard', Dashboard);

return {
    Dashboard:Dashboard,
};

});
