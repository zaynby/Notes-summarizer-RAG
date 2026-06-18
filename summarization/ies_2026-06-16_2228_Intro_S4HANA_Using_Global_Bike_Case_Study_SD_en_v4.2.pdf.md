# Intro_S4HANA_Using_Global_Bike_Case_Study_SD_en_v4.2.pdf
**Module:** ies
**Style:** structured_academic (experimenting)

# SAP S/4HANA Case Study: Global Bike Sales Process  

## Summary  

### [[Master Data]]  
- **Definition**: Centralized, reusable data in SAP systems that defines key entities (e.g., customers, materials, pricing conditions) to streamline business processes.  
- **Formula**: N/A  
- **Example**: Customer master data for *The Bike Zone* (e.g., address, payment terms) was created to simplify sales order processing.  

### [[Business Partner (BP)]]  
- **Definition**: A SAP entity representing organizations or individuals involved in business transactions (e.g., customers, vendors), assigned roles and attributes.  
- **Formula**: N/A  
- **Example**: *The Bike Zone* was created as a BP with the role **FLCU00 (FI Customer)** and assigned company code **US00**.  

### [[SAP Fiori Launchpad]]  
- **Definition**: A role-based, mobile-friendly interface in SAP systems providing access to apps and tasks.  
- **Formula**: N/A  
- **Example**: Used by **David Lopez** to access the *Manage Business Partner Master Data* app for creating customer records.  

### [[Manage Business Partner Master Data]]  
- **Definition**: SAP app for creating and maintaining Business Partner records, including organizational, role-specific, and address details.  
- **Formula**: N/A  
- **Example**: Used to create *The Bike Zone* with general data (e.g., **Street: 2144 N Orange Ave**, **City: Orlando**) and sales area details (e.g., **Sales Org: UE00**, **Currency: USD**).  

### [[Customer Request (Inquiry)]]  
- **Definition**: A non-binding customer request for information or quotation, documented in SAP to initiate the sales process.  
- **Formula**: N/A  
- **Example**: *The Bike Zone* submitted an inquiry for **5 Deluxe Touring Bikes (DXTR1###)** and **Professional Touring Bikes (DXTP1###)**.  

### [[Sales Order Process]]  
- **Definition**: A formal process in SAP to record customer orders, linking master data (customer, material) and conditions to trigger delivery and billing.  
- **Formula**: N/A  
- **Example**: A sales order was created referencing the quotation from *The Bike Zone*, including items like **DXTR1###** with quantity **5**.  

### [[Delivery Process]]  
- **Definition**: The SAP workflow for transferring goods to a customer, including stock checks, goods issue, and delivery documents.  
- **Formula**: N/A  
- **Example**: Goods were issued for *The Bike Zone* using delivery plant **MI00 (Miami)** and shipping condition **Standard**.  

### [[Billing Document]]  
- **Definition**: An SAP document generated after delivery to request payment, based on the sales order and delivery data.  
- **Formula**: N/A  
- **Example**: A customer invoice was created for *The Bike Zone* with payment term **0001 (Payable immediately)**.  

### [[Integrated Order-to-Cash Cycle]]  
- **Definition**: The end-to-end process in SAP from sales order creation to payment receipt, integrating SD, MM, and FI modules.  
- **Formula**: N/A  
- **Example**: *Global Bike* processed an order from inquiry to payment, involving roles like **Sales Representative**, **Warehouse Supervisor**, and **AR Accountant**.  

### [[Document Flow]]  
- **Definition**: A SAP tool tracking the sequence of documents (e.g., inquiry, quotation, sales order, delivery, invoice) to ensure data consistency.  
- **Formula**: N/A  
- **Example**: The document flow for *The Bike Zone* showed links between the sales order, delivery **D###**, and invoice **F###**.  

### [[SAP S/4HANA]]  
- **Definition**: SAP’s next-generation ERP suite built on the HANA in-memory database, enabling real-time integration across business functions.  
- **Formula**: N/A  
- **Example**: Used by *Global Bike* to synchronize sales, warehouse, and finance processes in real time.  

### [[SAP Sales & Distribution (SD Module)]]  
- **Definition**: A core SAP module managing sales processes, including order management, pricing, and delivery coordination.  
- **Formula**: N/A  
- **Example**: Steps like creating a sales order and managing Incoterms **FOB (Free on Board)** with location **Miami** were performed in SD.  

### [[Materials Management (MM Module)]]  
- **Definition**: SAP module handling material inventory, procurement, and stock management.  
- **Formula**: N/A  
- **Example**: Stock status for bikes like **DXTR1###** was checked in MM before confirming delivery.  

### [[Financial Accounting (FI Module)]]  
- **Definition**: SAP module for managing financial transactions, accounts receivable, and payment processing.  
- **Formula**: N/A  
- **Example**: Payment receipt for *The Bike Zone* was recorded in FI, updating the account **1200000 (Trade Receivables)**.  

---

**Note**: This summary links key SAP concepts and processes demonstrated in the Global Bike case study. Use [[Wikilinks]] to explore related terms in depth.