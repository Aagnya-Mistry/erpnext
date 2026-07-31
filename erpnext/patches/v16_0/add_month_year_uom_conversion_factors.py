import frappe


def execute():
	from erpnext.setup.setup_wizard.operations.install_fixtures import add_uom_data

	frappe.reload_doc("setup", "doctype", "UOM Conversion Factor")
	frappe.reload_doc("setup", "doctype", "UOM")
	frappe.reload_doc("stock", "doctype", "UOM Category")

	# add_uom_data only inserts UOMs and UOM Conversion Factors that don't already
	# exist, so this backfills the new Month/Year time conversion factors without
	# touching anything that's already there.
	add_uom_data()
