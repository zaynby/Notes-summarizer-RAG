# Intro_S4HANA_Using_Global_Bike_Slides_SD_en_v4.2.pptx
**Module:** ies
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided SAP S/4HANA Sales and Distribution (SD) content:

---

### **Sales and Distribution (SD) Module**
**Definition**: Core SAP module managing sales processes from order creation to payment, integrating organizational structures, master data, and transactional processes.  
**Formula**: N/A  
**Example**: Global Bike uses SD to manage customer orders, deliveries, and invoicing.

---

### **SD Organizational Structures**
#### **Company Code**
**Definition**: Smallest legal entity for financial reporting, containing all SD-relevant data.  
**Formula**: N/A  
**Example**: Global Bike's US company code "1000" handles legal compliance for sales in North America.

#### **Sales Organization**
**Definition**: Entity responsible for sales activities, including liability for products and customer claims.  
**Formula**: N/A  
**Example**: Global Bike's sales organization "2000" manages all bicycle sales in the US.

#### **Distribution Channel**
**Definition**: Path to deliver products/services (e.g., retail, wholesale).  
**Formula**: N/A  
**Example**: Global Bike uses channel "10" for direct online sales.

#### **Division**
**Definition**: Groups products/services for sales activities.  
**Formula**: N/A  
**Example**: Division "B10" represents mountain bikes in Global Bike's catalog.

---

### **SD Master Data**
#### **Customer Master**
**Definition**: Central repository for customer information (general, company code, and sales area data).  
**Formula**: N/A  
**Example**: Creating customer "The Bike Zone" in Orlando with sales area "2000-10-B10".

#### **Material Master**
**Definition**: Contains material specifications used across SAP modules (sales, production, procurement).  
**Formula**: N/A  
**Example**: Material "B100" represents Global Bike's flagship mountain bike.

#### **Condition Master (Pricing)**
**Definition**: Stores pricing elements (prices, discounts, taxes).  
**Formula**: Final Price = Base Price + Surcharges – Discounts + Taxes  
**Example**: Condition "PR00" (unit price $500) and "KWAPI" (5% discount) for material B100.

---

### **Order-to-Cash Process**
#### **Sales Order**
**Definition**: Document containing customer, material, pricing, delivery, and billing details.  
**Formula**: N/A  
**Example**: Order "4100000001" for 10 units of B100 to The Bike Zone.

#### **Availability Check (ATP)**
**Definition**: Determines material availability using forward/backward scheduling.  
**Formula**: ATP = Available Stock + Planned Receipts – Pending Requirements  
**Example**: System checks ATP for B100 to confirm delivery by 2023-12-01.

#### **Shipping & Route Determination**
**Definition**: Assigns shipping point and logistics route for delivery.  
**Formula**: N/A  
**Example**: Shipping point "1000" (Los Angeles warehouse) and route "TRK01" (truck delivery).

#### **Delivery Document**
**Definition**: Controls picking, packing, and goods issue.  
**Formula**: N/A  
**Example**: Delivery "8500000001" for sales order 4100000001.

#### **Billing Document**
**Definition**: Generates customer invoice based on sales order/delivery.  
**Formula**: Total Invoice = (Quantity × Price) + Taxes – Discounts  
**Example**: Invoice "8000000001" for delivery 8500000001.

#### **Payment Processing**
**Definition**: Final step where customer payment is posted and accounts reconciled.  
**Formula**: Cleared Amount = Invoice Amount – Payment + Discounts/Charges  
**Example**: Payment of $4,750 (95% of $5,000 invoice) received from The Bike Zone.

---

### **Key Integration Points**
1. **Master Data Integration**: Customer/Material Masters used across SD, MM, and FI modules.  
2. **Process Integration**:  
   - Sales Order → Delivery (via copy control)  
   - Delivery → Billing (order-based or delivery-based)  
   - Billing → Financial Accounting (automatic debit/credit postings)

---

### **[[Wikilinks]] to Related Concepts**
- [[SAP S/4HANA]]  
- [[Material Master]]  
- [[Customer Master]]  
- [[Order-to-Cash Process]]  
- [[Availability to Promise (ATP)]]  
- [[Goods Issue]]  

This summary aligns with the Global Bike case study, emphasizing practical application of SD concepts in a simulated business environment.