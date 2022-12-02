#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


def cafe():
    sales_target = pd.read_csv('sales targets.csv')
    outlets = pd.read_csv('sales_outlet.csv')
    sales_receipts = pd.read_csv('201904 sales reciepts.csv')
    product = pd.read_csv('product.csv')
    staff = pd.read_csv('staff.csv')
    customer = pd.read_csv('customer.csv')
    
    #No.1 Total sales per store in terms of revenue, excluding the warehouse
    tot_sales_per_store = sales_per_store(sales_receipts)
    print(f'(1). Total Sales per Store: \n{tot_sales_per_store}\n')
    
    #No.2 Total beans goal for all stores
    total_beans_goal = bean_goals(sales_target)
    print(f'(2). Total Beans Goal for all Stores = {total_beans_goal}\n')
    
    #No 3. Store neighbourhood with the highest merchandise goal target
    store_neighborhood = neighborhood(sales_target, outlets)
    print(f'(3). Store neighbourhood with the highest merchandise goal target = {store_neighborhood}\n')
    
    #No 4. Number of products sold per product group
    num_prod_per_group = product_per_group(sales_receipts, product)
    print(f'(4). Number of products sold per product group: \n{num_prod_per_group}\n')
    
    #No 5. Different employee positions in the company and number of employees per position
    position_count = employee_position(staff)
    print(f'(5). Different employee positions in the company and number of employees per position: \n{position_count}\n')
    
    #No 6. Most popular beverage product based on sales
    most_popular_beverage = popular_beverage(product, sales_receipts, 'most')
    print(f'(6). Most popular beverage product based on sales = {most_popular_beverage}\n')

    #No 7. Least popular beverage product based on sales
    least_popular_beverage = popular_beverage(product, sales_receipts, 'least')
    print(f'(7). Least popular beverage product based on sales = {least_popular_beverage}\n')
        
    #No 8. How many customers belong to each store - customer's with a "home" store
    customer_per_store = store_customers(customer)
    print(f'(8). Number of customers belonging to each home store: \n{customer_per_store}\n')
    
    #No 9. Which stores do not have any home customers, excluding the warehouse
    stores_no_home_cust = stores_without_home_customers(customer, outlets)
    print(f'(9). Stores not having any home customers, excluding the warehouse: \n{stores_no_home_cust}\n')    
    
    #No 10. Determine the gender distribution of customers
    cust_gender_dist = gender_dist(customer)
    print(f'(10). The Gender Distribution of Customers (M or F): \n{cust_gender_dist}\n')    
    


# In[3]:


def sales_per_store(sales_receipts):
    sales_receipts['Revenue'] = sales_receipts['quantity'] * sales_receipts['unit_price']
    tot = sales_receipts[['sales_outlet_id', 'Revenue']].groupby('sales_outlet_id').sum().reset_index()
    return tot


# In[4]:


def bean_goals(sales_target):
    bean_target = sales_target['beans_goal'].sum()
    return bean_target


# In[5]:


def neighborhood(sales_target, outlets):
    s_id = sales_target['merchandise _goal'].max()
    outlet_id = sales_target.sales_outlet_id[sales_target['merchandise _goal'] == s_id].tolist()
    name = outlets.Neighorhood[outlets['sales_outlet_id'] == outlet_id[0]].tolist()
    return name[0]


# In[6]:


def product_per_group(sales_receipts, product):
    prod_id = sales_receipts[['product_id', 'quantity']].groupby('product_id').sum().reset_index()
    grp = product[['product_group', 'product_id']]
    prod_group = grp.merge(prod_id, how='inner', on='product_id')
    product_grp = prod_group[['product_group', 'quantity']].groupby('product_group').sum().reset_index()
    return product_grp


# In[7]:


def employee_position(staff):
    st_count = staff['position'].value_counts()
    return st_count


# In[8]:


def popular_beverage(product, sales_receipts, cond):
    ids = product[['product_id', 'product_group', 'product']][product['product_group'] == 'Beverages']
    prod_id = sales_receipts[['product_id', 'quantity']].groupby('product_id').sum().reset_index()
    beverages = ids.merge(prod_id, how='inner', on='product_id')
    most = beverages[beverages['product_id'] == beverages.product_id.max()]
    least = beverages[beverages['product_id'] == beverages.product_id.min()]
    most = most['product'].tolist()
    least = least['product'].tolist()
    if cond == 'most':
        return most[0]
    elif cond == 'least':
        return least[0]


# In[9]:


def store_customers(customer):
    cust = customer[['home_store', 'customer_id']].groupby('home_store').count().reset_index()
    cust['customer_count'] = cust['customer_id']
    cust_count = cust[['home_store', 'customer_count']]
    return cust_count


# In[10]:


def stores_without_home_customers(customer, outlets):
    store_no = customer.home_store.unique()
    no_home_cust = outlets[(outlets['sales_outlet_id'].isin(store_no) == False) & (outlets['sales_outlet_type'] != 'warehouse')]
    return no_home_cust[['sales_outlet_id', 'store_address', 'sales_outlet_type']]


# In[11]:


def gender_dist(customer):
    cust_gender = customer[customer['gender'].isin(['M', 'F'])]
    return cust_gender.gender.value_counts()


# In[12]:


cafe()

