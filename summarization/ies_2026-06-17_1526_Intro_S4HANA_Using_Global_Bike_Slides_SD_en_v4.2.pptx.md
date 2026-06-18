# Intro_S4HANA_Using_Global_Bike_Slides_SD_en_v4.2.pptx
**Module:** ies
**Style:** structured_academic (experimenting)

Here’s a structured summary of the **Sales and Distribution (SD)** module content using the required format:

---

### **SD Organizational Structures**
#### **Client**  
- **Definition**: An independent environment in the SAP system, logically separated from others.  
- **Formula**: N/A  
- **Example**: Global Bike operates multiple clients for testing, training, and production.  

#### **Company Code**  
- **Definition**: Smallest organizational unit for maintaining legal financial books (e.g., accounting, tax compliance).  
- **Formula**: N/A  
- **Example**: Global Bike’s company code "1000" manages financial reporting for its European operations.  

#### **Sales Organization**  
- **Definition**: Unit responsible for selling products/services, including legal liability.  
- **Formula**: N/A  
- **Example**: Global Bike’s sales organization "4100" handles bicycle sales in North America.  

#### **Distribution Channel**  
- **Definition**: Method of delivering products/services to customers (e.g., retail, wholesale).  
- **Formula**: N/A  
- **Example**: Global Bike uses a direct distribution channel for online sales.  

#### **Division**  
- **Definition**: Groups materials/products for sales activities.  
- **Formula**: N/A  
- **Example**: Division "10" represents mountain bikes in Global Bike’s product portfolio.  

#### **Sales Area**  
- **Definition**: Combination of Sales Organization, Distribution Channel, and Division.  
- **Formula**: Sales Area = Sales Org + Distribution Channel + Division  
- **Example**: Sales Area "4100-10-01" (Sales Org 4100, Distribution Channel 10, Division 01).  

---

### **SD Master Data**
#### **Customer Master Record**  
- **Definition**: Central repository for customer information (e.g., payment terms, contact details).  
- **Formula**: N/A  
- **Example**: Customer "C1001" (ABC Retail) has a master record with billing address and credit limit.  

#### **Material Master Record**  
- **Definition**: Stores material-specific data (e.g., pricing, storage conditions).  
- **Formula**: N/A  
- **Example**: Material "Bike-001" (Mountain Bike) includes weight, dimensions, and pricing.  

#### **Condition Master Data (Pricing)**  
- **Definition**: Defines pricing elements (e.g., discounts, taxes, surcharges).  
- **Formula**: Final Price = Base Price + Surcharges – Discounts + Taxes  
- **Example**: Condition "MWST" (8% tax) applies to sales in Germany.  

---

### **SD Processes: Order-to-Cash**
#### **Sales Order**  
- **Definition**: Legally binding document confirming customer intent to purchase.  
- **Formula**: N/A  
- **Example**: Sales Order "4200012345" for 50 bicycles with delivery by 2023-12-31.  

#### **Delivery Creation**  
- **Definition**: Process of generating a delivery document from a sales order.  
- **Formula**: N/A  
- **Example**: Delivery "D12345" created for Sales Order "4200012345".  

#### **Goods Issue**  
- **Definition**: Event marking the physical transfer of goods to the customer.  
- **Formula**: Inventory Adjustment = Quantity Shipped  
- **Example**: Goods Issue posted for Delivery "D12345", reducing warehouse stock by 50 units.  

#### **Billing**  
- **Definition**: Process of generating an invoice based on the delivery or sales order.  
- **Formula**: Invoice Amount = Quantity × Price + Taxes  
- **Example**: Invoice "INV12345" for $10,000 created from Delivery "D12345".  

#### **Payment**  
- **Definition**: Customer payment received against an invoice.  
- **Formula**: Account Receivable Reduction = Payment Amount  
- **Example**: Customer "C1001" pays $10,000 via bank transfer.  

---

### **Key SD Concepts**
#### **Availability Check (ATP)**  
- **Definition**: System check to confirm material availability for a sales order.  
- **Formula**: ATP = Available Stock – Reserved Quantity – Pending Deliveries  
- **Example**: ATP check for "Bike-001" shows 200 units available for order "4200012345".  

#### **Credit Check**  
- **Definition**: Verification of customer credit limit before order confirmation.  
- **Formula**: Available Credit = Total Credit Limit – Open Orders – Invoices  
- **Example**: Credit check for "C1001" shows $50,000 available out of $100,000 limit.  

#### **Output**  
- **Definition**: Customer communication (e.g., order confirmations, invoices) via EDI, email, etc.  
- **Formula**: N/A  
- **Example**: Order confirmation sent via email to "C1001" for Sales Order "4200012345".  

---

### **Document Flow**  
- **Definition**: Tracking of all documents (sales order, delivery, invoice) in the order-to-cash process.  
- **Formula**: N/A  
- **Example**: Document flow for Sales Order "4200012345" shows linked Delivery "D12345" and Invoice "INV12345".  

---

### **Integration Points**  
- **SD-MM Integration**: Transfer of requirements from sales orders to Material Management for procurement.  
- **SD-FI Integration**: Billing documents update Financial Accounting (FI) for revenue recognition.  
- **SD-WM Integration**: Delivery processes integrated with Warehouse Management for picking and packing.  

---

**Wikilinks**:  
- [[Sales Organization]]  
- [[Material Master Record]]  
- [[Order-to-Cash Process]]  
- [[Goods Issue]]  
- [[Availability Check]]  

This summary aligns with the S/4HANA Global Bike curriculum, focusing on SD organizational structures, master data, and the order-to-cash process.