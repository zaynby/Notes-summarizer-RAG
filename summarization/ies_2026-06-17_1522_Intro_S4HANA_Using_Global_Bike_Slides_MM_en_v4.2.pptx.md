# Intro_S4HANA_Using_Global_Bike_Slides_MM_en_v4.2.pptx
**Module:** ies
**Style:** structured_academic (experimenting)

## Materials Management (MM) in S/4HANA: Overview and Processes

### Materials Management (MM)
**Term:** Materials Management (MM)

**Definition:** A comprehensive system for managing materials, from procurement to inventory control. It ensures efficient management of materials across various organizational levels.

**Formula:** Not applicable; however, the MM process involves several steps:
1. **Create Material Master Records**
2. **Create Vendor Master Records**
3. **Generate Purchase Requisitions and Orders**
4. **Process Goods Receipts**
5. **Manage Invoices and Payments**

### S/4HANA 2022
**Term:** S/4HANA 2022

**Definition:** A version of SAP S/4HANA that introduces Fiori 3.0, enhancing user experience with a modern interface.

**Formula:** Not applicable; however, it supports the MM processes described above.

### Client and Company Code
**Term:** Client

**Definition:** An independent environment in the system where data is stored and processed.

**Formula:** 
- **Client =** Independent environment within S/4HANA.

**Example:**
- A company might have multiple clients, each representing a different business unit or legal entity.

### Company Code
**Term:** Company Code

**Definition:** The smallest organizational unit for which you can maintain a set of books in the SAP system.

**Formula:** 
- **Company Code =** Smallest independent accounting unit within a client.

### Plant
**Term:** Plant

**Definition:** An operating area or branch within a company, such as manufacturing, distribution, purchasing, or maintenance facility.

**Formula:**
- **Plant =** Operating area for material handling and production.

### Storage Location
**Term:** Storage Location

**Definition:** An organizational unit allowing differentiation between the various stocks of a material in a plant.

**Formula:**
- **Storage Location =** Unique identifier for stock within a plant.

### Purchase-to-Pay Business Process
**Term:** Purchase-to-Pay (P2P)

**Definition:** A business process that includes activities from creating purchase requisitions to receiving goods and paying invoices.

**Key Activities:**
1. **Create Material Master Record**
2. **Create Vendor Master Record**
3. **Generate Purchase Requisition**
4. **Create Purchase Order**
5. **Post Goods Receipt**
6. **Enter Vendor Invoice**
7. **Process Automatic Payment Run**

### MM Organizational Structure
**Term:** Materials Management (MM) Organizational Structure

**Definition:** Hierarchical structure within the company that supports the P2P process.

**Formula:**
- **Organizational Levels:**
  - **Client**
  - **Company Code**
  - **Plant**
  - **Storage Location**

### Purchasing Organization
**Term:** Purchasing Organization

**Definition:** An organization unit responsible for procuring services and materials, negotiating conditions with vendors.

**Formula:**
- **Purchasing Organization =** Unit that handles procurement activities.

### Purchasing Group
**Term:** Purchasing Group

**Definition:** A key representing the buyer or group of buyers who are responsible for certain purchasing activities.

**Formula:**
- **Purchasing Group =** Key for grouping similar purchasing activities.

### Vendor Master Data
**Term:** Vendor Master

**Definition:** A record containing all necessary information needed to do business with an external supplier, maintained by Purchasing and Accounting Departments.

**Formula:**
- **Vendor Master =** Central business partner master record with roles like FI Vendor or Vendor.

### Material Master Data
**Term:** Material Master

**Definition:** Information a company needs to manage about materials used in various processes (Sales & Distribution, Materials Management, Production, etc.).

**Formula:**
- **Material Master =** Data stored in functional segments called Views.

### Purchasing Information Record (PIR)
**Term:** Purchasing Information Record

**Definition:** A record that contains data on pricing and conditions for specific materials, used as default information for Purchase Orders.

**Formula:**
- **PIR =** Key information for sourcing materials from vendors.

### Procure-to-Pay Process
**Term:** Procure-to-Pay (P2P) Process

**Definition:** The process of requesting goods or services and ensuring they are received, invoiced, and paid correctly.

**Formula:**
1. **Create Purchase Requisition**
2. **Generate Purchase Order**
3. **Receive Goods**
4. **Process Invoice**
5. **Make Payment**

### Goods Receipt
**Term:** Goods Receipt

**Definition:** The process of accepting goods into the system after they have been delivered against a purchase order.

**Formula:**
- **Goods Receipt =** Movement type (e.g., 101) that updates inventory and accounting documents.

### Invoice Processing
**Term:** Invoice Processing

**Definition:** The verification and posting of incoming invoices to ensure accurate financial records.

**Formula:**
- **Invoice Processing =** Verification, update material master, create accounting document, post invoice.

### Payment Process
**Term:** Payment Process

**Definition:** The process of making payments to vendors based on verified invoices.

**Formula:**
- **Payment Process =** Post outgoing payment vs. payment program, calculate payment amount, print payment medium, record transaction in financial accounting.

### Integration Points
**Term:** FI-MM Integration Point

**Definition:** The point where Financial Accounting (FI) and Materials Management (MM) systems integrate to ensure accurate financial records and material transactions.

**Formula:**
- **Integration =** Reconciliation of goods receipts and invoices with vendor payments.