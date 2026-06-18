# Intro_S4HANA_Using_Global_Bike_Case_Study_SD_en_v4.2.pdf
**Module:** ies
**Style:** structured_academic (experimenting)

Here’s a structured academic summary of the provided SAP S/4HANA Sales and Distribution (SD) case study content:

---

### **Sales and Distribution (SD) Master Data Creation**

#### **Business Partner (BP) Master Data**  
**Definition**: Central repository for customer and vendor information, including roles (e.g., customer, vendor) and organizational assignments.  
**Formula**: N/A  
**Example**: Creating "The Bike Zone" as a customer in Orlando with BP roles FLCU00 (FI Customer) and FLCU01 (Sales Customer).  

---

#### **Customer Master Data**  
**Definition**: Subset of BP master data containing sales and accounting details for customers.  
**Formula**: N/A  
**Example**: Assigning company code US00, reconciliation account 1200000, and payment term 0001 for "The Bike Zone".  

---

#### **Contact Person**  
**Definition**: Individual associated with a customer or vendor, stored as a BP with role BUP001 (Contact Person).  
**Formula**: N/A  
**Example**: Creating a contact person "John Doe###" linked to "The Bike Zone".  

---

#### **BP Relationship**  
**Definition**: Link between business partners (e.g., assigning a contact person to a customer).  
**Formula**: N/A  
**Example**: Associating contact person BP number ___ with customer BP number ___ in the "Contacts" tab.  

---

#### **Customer Inquiry (Sales Request)**  
**Definition**: Non-binding customer request for product or pricing information, processed into a quotation.  
**Formula**: N/A  
**Example**: Creating an inquiry for "The Bike Zone" with materials "Deluxe Touring Bike (black)" (DXTR1###) and "Professional Touring Bike (black)" (PRTR1###), each with a quantity of 5.  

---

### **SD Organizational Structures**  

#### **Sales Area**  
**Definition**: Combination of Sales Organization, Distribution Channel, and Division.  
**Formula**: Sales Area = Sales Org + Distribution Channel + Division  
**Example**: Sales Area "UE00-WH-BI" (Sales Org UE00, Channel WH, Division BI).  

---

#### **Company Code**  
**Definition**: Smallest legal entity for financial reporting in SAP.  
**Formula**: N/A  
**Example**: Company code "US00" for Global Bike Inc.’s US operations.  

---

### **SD Processes**  

#### **Order-to-Cash Process**  
**Definition**: Integrated cycle from sales order creation to payment processing.  
**Formula**: N/A  
**Example**: Creating a sales order referencing a quotation, delivering goods, billing, and posting customer payment.  

---

### **Key Integration Points**  
1. **Master Data Integration**: Customer and material masters are reused across SD, MM (Materials Management), and FI (Financial Accounting).  
2. **Process Integration**:  
   - Sales Order → Delivery (via copy control)  
   - Delivery → Billing (order-based or delivery-based)  
   - Billing → Financial Accounting (automatic debit/credit postings)  

---

### **[[Wikilinks]] to Related Concepts**  
- [[Business Partner]]  
- [[Master Data]]  
- [[Sales Order]]  
- [[Customer Inquiry]]  
- [[Order-to-Cash Process]]  
- [[Sales Area]]  

---

**Note**: This summary focuses on master data creation and initial SD processes from the case study. Additional steps (e.g., delivery, billing) are implied but not detailed in the provided content. For full process coverage, refer to subsequent steps in the case study.