from CyberSource import *
from pathlib import Path
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

create_invoice_path = os.path.join(os.getcwd(), "samples", "Invoicing", "Invoices", "create-draft-invoice.py")
create_invoice = SourceFileLoader("module.name", create_invoice_path).load_module()


# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d


def update_invoice():
    invoice_id = create_invoice.create_draft_invoice().id
    customerInformationName = "New Customer Name"
    customerInformationEmail = "new_email@my-email.world"
    customerInformation = Invoicingv2invoicesCustomerInformation(
        name = customerInformationName,
        email = customerInformationEmail
    )

    invoiceInformationDescription = "This is after updating invoice"
    invoiceInformationDueDate = "2019-07-11"
    invoiceInformationAllowPartialPayments = True
    invoiceInformationDeliveryMode = "none"
    invoiceInformation = Invoicingv2invoicesidInvoiceInformation(
        description = invoiceInformationDescription,
        due_date = invoiceInformationDueDate,
        allow_partial_payments = invoiceInformationAllowPartialPayments,
        delivery_mode = invoiceInformationDeliveryMode
    )

    orderInformationAmountDetailsTotalAmount = "2623.64"
    orderInformationAmountDetailsCurrency = "USD"
    orderInformationAmountDetailsDiscountAmount = "126.08"
    orderInformationAmountDetailsDiscountPercent = 5.00
    orderInformationAmountDetailsSubAmount = 2749.72
    orderInformationAmountDetailsMinimumPartialAmount = 20.00
    orderInformationAmountDetailsTaxDetailsType = "State Tax"
    orderInformationAmountDetailsTaxDetailsAmount = "208.00"
    orderInformationAmountDetailsTaxDetailsRate = "8.25"
    orderInformationAmountDetailsTaxDetails = Invoicingv2invoicesOrderInformationAmountDetailsTaxDetails(
        type = orderInformationAmountDetailsTaxDetailsType,
        amount = orderInformationAmountDetailsTaxDetailsAmount,
        rate = orderInformationAmountDetailsTaxDetailsRate
    )

    orderInformationAmountDetailsFreightAmount = "20.00"
    orderInformationAmountDetailsFreightTaxable = True
    orderInformationAmountDetailsFreight = Invoicingv2invoicesOrderInformationAmountDetailsFreight(
        amount = orderInformationAmountDetailsFreightAmount,
        taxable = orderInformationAmountDetailsFreightTaxable
    )

    orderInformationAmountDetails = Invoicingv2invoicesOrderInformationAmountDetails(
        total_amount = orderInformationAmountDetailsTotalAmount,
        currency = orderInformationAmountDetailsCurrency,
        discount_amount = orderInformationAmountDetailsDiscountAmount,
        discount_percent = orderInformationAmountDetailsDiscountPercent,
        sub_amount = orderInformationAmountDetailsSubAmount,
        minimum_partial_amount = orderInformationAmountDetailsMinimumPartialAmount,
        tax_details = orderInformationAmountDetailsTaxDetails.__dict__,
        freight = orderInformationAmountDetailsFreight.__dict__
    )

    orderInformationLineItems = []
    orderInformationLineItems1 = Invoicingv2invoicesOrderInformationLineItems(
        product_sku = "P653727383",
        product_name = "First line item's name",
        quantity = 21,
        unit_price = "120.08"
    )

    orderInformationLineItems.append(orderInformationLineItems1.__dict__)

    orderInformation = Invoicingv2invoicesOrderInformation(
        amount_details = orderInformationAmountDetails.__dict__,
        line_items = orderInformationLineItems
    )

    requestObj = UpdateInvoiceRequest(
        customer_information = customerInformation.__dict__,
        invoice_information = invoiceInformation.__dict__,
        order_information = orderInformation.__dict__
    )

    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = InvoicesApi(client_config)
        return_data, status, body = api_instance.update_invoice(invoice_id, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        write_log_audit(status)
        return return_data
    except Exception as e:
        write_log_audit(e.status if hasattr(e, 'status') else 999)
        print("\nException when calling InvoicesApi->update_invoice: %s\n" % e)


def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")


if __name__ == "__main__":
    update_invoice()
