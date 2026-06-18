# Intro_S4HANA_Using_Global_Bike_Exercises_SD_en_v4.2.pdf
**Module:** ies
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided SAP S/4HANA Sales and Distribution (SD) case study content:

---

### **Business Partner (BP)**  
**Definition**: A unified entity representing organizations, persons, or groups with which a company has a business interest. Combines master data for customers, suppliers, and contact persons.  
**Formula**: None  
**Example**: Beantown Bikes (customer) with a unique BP number. Roles include *FI Customer* (financial accounting) and *Customer* (sales).  

---

### **BP Roles**  
**Definition**: Specific functions a business partner performs in business processes (e.g., sales, finance).  
**Formula**: None  
**Example**:  
- *Customer (FLCU01)*: Sales-related transactions.  
- *FI Customer*: Financial accounting (e.g., payment terms).  

---

### **General Data (BP)**  
**Definition**: Company-wide information independent of BP roles (e.g., name, address, communication details).  
**Formula**: None  
**Example**: Beantown Bikes’ global name and Boston address visible across departments.  

---

### **Sales Order**  
**Definition**: A document confirming a customer’s order, containing header (overall details) and item (product-specific) data.  
**Formula**: Net Value = Quantity × Price  
**Example**:  
- Order #1 for 5 Deluxe Touring Bikes (black) at $3,000 each.  
- Net Value = 5 × $3,000 = **$15,000**.  

---

### **Document Header/Items**  
**Definition**:  
- **Header**: Data valid for the entire document (e.g., order date, customer).  
- **Items**: Data specific to individual products (e.g., quantity, price).  
**Formula**: Profit per Item = Selling Price − Cost Price  
**Example**:  
- Deluxe Touring Bike: $3,000 (selling) − $1,400 (cost) = **$1,600 profit**.  

---

### **Outbound Delivery**  
**Definition**: A document representing the physical delivery of goods to a customer.  
**Formula**: None  
**Example**: Delivery #80000000 for Order #1, status *Completed*, with 5 bicycles delivered.  

---

### **Billing Document**  
**Definition**: A financial claim for payment generated after delivery.  
**Formula**: Total Claim = Net Value from Sales Order  
**Example**: Billing Document #90000001 for $15,000 (linked to Order #1).  

---

### **Document Flow**  
**Definition**: A tool tracking the sequence of sales and accounting documents (e.g., order → delivery → invoice).  
**Formula**: None  
**Example**:  
- **Operational Flow**: Sales Order #1 → Delivery #80000000 → Billing #90000001.  
- **G/L Flow**: Links to general ledger postings (e.g., revenue, accounts receivable).  

---

### **T-Accounts**  
**Definition**: Visual representation of debit and credit postings in accounting.  
**Formula**: Debit = Credit  
**Example**: Goods Issue Document triggers debit to *Accounts Receivable* and credit to *Revenue*.  

---

### **Sales Areas**  
**Definition**: Structural organizational units defining sales processes (company code, sales organization, distribution channel).  
**Formula**: None  
**Example**: Company Code *US00* (Global Bike Inc.) linked to Beantown Bikes.  

---

### **Pricing Elements**  
**Definition**: Breakdown of components affecting the final price (e.g., base price, discounts, profits).  
**Formula**: Net Price = Base Price − Discounts + Supplements  
**Example**: Deluxe Touring Bike’s $3,000 price includes $1,400 cost and $1,600 profit.  

---

### **Process Flow**  
**Definition**: A chronological view of document relationships in the sales cycle.  
**Formula**: None  
**Example**: Order #1 → Delivery #80000000 → Billing #90000001 displayed in the Process Flow tab.  

---

**Key Links**:  
- [[Business Partner]] → [[Sales Order]] → [[Outbound Delivery]] → [[Billing Document]] → [[Document Flow]]  
- [[T-Accounts]] → [[General Ledger (G/L)]]  

This summary captures core SD concepts, their interrelationships, and practical examples from the Global Bike case study.