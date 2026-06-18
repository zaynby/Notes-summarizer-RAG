# Intro_S4HANA_Using_Global_Bike_Exercises_SD_en_v4.2.pdf
**Module:** ies
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided SAP S/4HANA case study exercises:

---

### **Business Partner (BP)**  
**Definition**: A unified entity in SAP S/4HANA representing organizations, persons, or groups with which a company has a business interest. Combines general data (name, address) and role-specific data (customer, supplier).  
**Formula**: N/A  
**Example**: Beantown Bikes is a BP with roles "FI Customer" and "Customer" (SD Exercise 1).  

---

### **Customer Master Data**  
**Definition**: Centralized data storage for customer information, divided into:  
1. **General Data**: Global names, addresses (visible to all departments).  
2. **Accounting Data**: Company codes, payment terms.  
3. **Sales Data**: Sales areas, pricing.  
**Formula**: N/A  
**Example**: Beantown Bikes' master data includes general address details and sales area specifications (SD Exercise 1).  

---

### **Sales Order**  
**Definition**: A document confirming a customer’s order, consisting of:  
- **Document Header**: Overall data (customer, total value).  
- **Document Items**: Product-specific details (quantity, price).  
**Formula**:  
Net Value = (Unit Price × Quantity) ± Discounts/Surcharges  
**Example**: Sales Order #1 for 5 Deluxe Touring Bikes (5 × $3,000 = $15,000) (SD Exercise 2).  

---

### **Outbound Delivery**  
**Definition**: A document representing the physical transfer of goods to a customer, linked to a sales order. Includes details like delivery date and picking status.  
**Formula**: N/A  
**Example**: Delivery #80000000 for 5 bicycles to Beantown Bikes (SD Exercise 3).  

---

### **Billing Document**  
**Definition**: A financial document requesting payment from a customer, generated after delivery. Includes pricing elements like list price and profit.  
**Formula**:  
Total Invoice Value = (Unit Price × Quantity)  
**Example**: Billing Document #90000001 for $15,000 (5 × $3,000) (SD Exercise 4).  

---

### **Document Flow**  
**Definition**: A tool tracking the sequence of documents in a sales process, including:  
- **Operational Document Flow**: Sales order → Delivery → Invoice.  
- **G/L Document Flow**: Accounting postings (e.g., revenue, receivables).  
**Formula**: N/A  
**Example**: Sales Order #1 → Delivery #80000000 → Billing Document #90000001 (SD Exercise 5).  

---

### **T-Account View**  
**Definition**: A visualization of accounting postings following the "debit to credit" principle.  
**Formula**:  
Debit = Credit  
**Example**: Goods Issue posts debit to Inventory (Asset) and credit to Cost of Goods Sold (Expense) (SD Exercise 5).  

---

### **Key Apps & Transactions**  
| **App/Transaction**                | **Purpose**                                      |  
|------------------------------------|--------------------------------------------------|  
| **Manage Business Partner Master Data** | Create/view BP data (general, roles, sales areas) |  
| **Manage Sales Orders**            | Display/edit sales orders and document flow       |  
| **Manage Outbound Deliveries**    | Track delivery status and item details            |  
| **Manage Billing Documents**      | Review invoices and pricing elements              |  

---

### **Wikilinks**  
- [[Business Partner]] → [[Customer Master Data]], [[Sales Order]]  
- [[Sales Order]] → [[Outbound Delivery]], [[Billing Document]]  
- [[Document Flow]] → [[T-Account View]], [[G/L Document Flow]]  

This summary integrates core concepts from the exercises, emphasizing SAP S/4HANA’s data structure and process flow. Each term is contextualized with examples from the Global Bike case study.