# Intro_S4HANA_Using_Global_Bike_Slides_MM_en_v4.2.pptx
**Module:** ies
**Style:** structured_academic (experimenting)

Here’s a structured summary of the Materials Management (MM) content in S/4HANA using the Global Bike case study:

---

### **Key Terms and Concepts**

#### **1. Organizational Structure in MM**
**Term**: [[Client]]  
- **Definition**: An independent environment in the SAP system.  
- **Formula**: N/A  
- **Example**: Global Bike operates multiple clients for testing, production, and training.  

**Term**: [[Company Code]]  
- **Definition**: The smallest organizational unit for maintaining a legal set of books (e.g., financial reporting).  
- **Formula**: N/A  
- **Example**: Global Bike’s US operations might use company code "1000" for legal compliance.  

**Term**: [[Plant]]  
- **Definition**: An operational facility (e.g., manufacturing, distribution, or purchasing site).  
- **Formula**: N/A  
- **Example**: Global Bike’s warehouse in Orlando is designated as a plant.  

**Term**: [[Storage Location]]  
- **Definition**: An organizational unit to differentiate stock within a plant.  
- **Formula**: N/A  
- **Example**: Stock in the "North Wing" vs. "South Wing" of a warehouse.  

---

#### **2. Master Data in MM**  
**Term**: [[Vendor Master Data]]  
- **Definition**: Centralized record containing all vendor information (e.g., addresses, payment terms, bank details).  
- **Formula**: N/A  
- **Example**: Global Bike creates a vendor master record for "Cycle Parts Inc." with roles FLVN00 (FI Vendor) and FLVN01 (Vendor).  

**Term**: [[Material Master Data]]  
- **Definition**: Comprehensive record of material information (e.g., description, pricing, storage details).  
- **Formula**: N/A  
- **Example**: Global Bike’s material master for "Mountain Bike Frame" includes data for sales, production, and inventory.  

**Term**: [[Purchasing Information Record]]  
- **Definition**: Stores vendor-specific material data (e.g., pricing, delivery times).  
- **Formula**: N/A  
- **Example**: A record linking vendor "Cycle Parts Inc." to material "Bike Chain" with a unit price of $5.  

---

#### **3. Procure-to-Pay Process**  
**Term**: [[Purchase Requisition]]  
- **Definition**: Internal document requesting procurement of goods/services.  
- **Formula**: N/A  
- **Example**: Global Bike’s warehouse creates a requisition for 100 bike tires.  

**Term**: [[Source List]]  
- **Definition**: Specifies approved suppliers for a material in a plant.  
- **Formula**: N/A  
- **Example**: Source list directs purchase of tires only from pre-approved vendors like "TirePro."  

**Term**: [[Purchase Order (PO)]]  
- **Definition**: Formal request to a vendor for materials/services under defined terms.  
- **Formula**: N/A  
- **Example**: Global Bike issues PO "4200000012" to "Cycle Parts Inc." for 100 bike frames.  

**Term**: [[Goods Receipt]]  
- **Definition**: Process of logging received goods into the system.  
- **Formula**: N/A  
- **Example**: Warehouse staff record receipt of 100 bike frames against PO "4200000012" using movement type **101** (goods receipt into warehouse).  

**Term**: [[Invoice Processing]]  
- **Definition**: Verifying and posting vendor invoices against goods receipts and POs.  
- **Formula**: N/A  
- **Example**: Global Bike’s accountant processes an invoice from "Cycle Parts Inc.," matching it to PO "4200000012."  

**Term**: [[Vendor Payment]]  
- **Definition**: Settlement of payments to vendors.  
- **Formula**: N/A  
- **Example**: Global Bike runs a payment program to pay "Cycle Parts Inc." via bank transfer.  

---

#### **4. Integration Points**  
**Term**: [[FI-MM Integration]]  
- **Definition**: Link between Financial Accounting (FI) and Materials Management (MM) for financial transactions.  
- **Formula**: N/A  
- **Example**: Goods receipt and invoice processing trigger accounting entries in FI (e.g., liabilities, asset accounts).  

---

### **Key Processes**  
1. **Vendor Master Creation**: Centralized business partner setup with roles (FLVN00, FLVN01).  
2. **Material Master Creation**: Defines material attributes across modules (sales, production, inventory).  
3. **Procure-to-Pay Workflow**:  
   - Purchase Requisition → Source List/RFQ → Purchase Order → Goods Receipt → Invoice Processing → Vendor Payment.  
4. **Warehouse Management**: Movement types (e.g., 101, 103) track stock changes.  

---

### **Learning Objectives**  
By the end of this module, students should be able to:  
1. Describe the procure-to-pay process.  
2. Create vendor and material master records.  
3. Process purchase requisitions, orders, goods receipts, and invoices.  
4. Explain integration with Financial Accounting (FI).  

---

**Linked Concepts**:  
[[Purchase Order]] → [[Goods Receipt]] → [[Invoice Processing]] → [[Vendor Payment]]  
[[Client]] → [[Company Code]] → [[Plant]] → [[Storage Location]]  
[[Vendor Master Data]] ↔ [[Material Master Data]] → [[Purchasing Information Record]]  

This summary aligns with the S/4HANA MM curriculum for Global Bike, emphasizing practical workflows and system integration.