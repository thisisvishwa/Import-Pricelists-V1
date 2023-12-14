odoo.define('odoo_pricelist_import.import_button', function (require) {
    "use strict";

    var core = require('web.core');
    var Sidebar = require('web.Sidebar');
    var _t = core._t;

    Sidebar.include({
        _redraw: function () {
            var self = this;
            this._super.apply(this, arguments);
            if (this.env.model === 'product.pricelist') {
                this.items.other.push({
                    label: _t("Import Pricelist from Excel"),
                    callback: self.on_click_import_pricelist,
                    classname: 'o_import_excel'
                });
            }
        },

        on_click_import_pricelist: function () {
            var self = this;
            var action = {
                type: 'ir.actions.act_window',
                res_model: 'pricelist.import.wizard',
                view_mode: 'form',
                view_type: 'form',
                views: [[false, 'form']],
                target: 'new',
                context: {
                    'default_pricelist_id': self.env.activeIds[0],
                },
            };
            return self.do_action(action);
        },
    });
});