# apps/shipping/bluedart_client.py

import requests
import xml.etree.ElementTree as ET # BlueDart APIs often use SOAP/XML
from django.conf import settings

class BlueDartClient:
    def __init__(self):
        self.login_id = settings.BLUEDART_API_LOGIN_ID
        self.license_key = settings.BLUEDART_API_LICENSE_KEY
        self.customer_code = settings.BLUEDART_API_CUSTOMER_CODE
        
        # BlueDart provides different URLs for Staging (testing) and Production
        if settings.BLUEDART_IS_PRODUCTION:
            self.waybill_generation_url = "https://netconnect.bluedart.com/Ver1.8/ShippingAPI/WayBill/WayBillGeneration.svc"
            self.tracking_url = "https://netconnect.bluedart.com/Ver1.8/ShippingAPI/Track/Track.svc"
        else:
            # Use the Staging/Testing URLs provided by BlueDart
            self.waybill_generation_url = "https://netconnect.bluedart.com/Ver1.8/Demo/ShippingAPI/WayBill/WayBillGeneration.svc"
            self.tracking_url = "https://netconnect.bluedart.com/Ver1.8/Demo/ShippingAPI/Track/Track.svc"
            

    def create_shipment(self, order, shipping_addr):
        """
        Calls the BlueDart WayBillGeneration API to create a shipment.
        
        NOTE: This is a conceptual example. You MUST adapt the XML payload
        to match the exact specification in the BlueDart API documentation.
        """
        headers = {'Content-Type': 'application/soap+xml; charset=utf-8'}

        # 1. Construct the XML payload based on BlueDart's documentation
        # Map Oscar's order and address objects to BlueDart's required fields.
        payload = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" ...>
           <soapenv:Header/>
           <soapenv:Body>
              <GenerateWayBill>
                 <Request>
                    <Profile>
                       <Api_type>S</Api_type>
                       <LicentKey>{self.license_key}</LicentKey>
                       <LoginID>{self.login_id}</LoginID>
                       <Version>1.8</Version>
                    </Profile>
                    <Shipment>
                       <Shipper>
                          <!-- Your company's details -->
                       </Shipper>
                       <Consignee>
                          <ConsigneeName>{shipping_addr.name}</ConsigneeName>
                          <ConsigneeAddress1>{shipping_addr.line1}</ConsigneeAddress1>
                          <ConsigneeAddress2>{shipping_addr.line2}</ConsigneeAddress2>
                          <ConsigneePincode>{shipping_addr.postcode}</ConsigneePincode>
                          <ConsigneeTelephone>{shipping_addr.phone_number}</ConsigneeTelephone>
                       </Consignee>
                       <Services>
                          <Commodity>
                             <CommodityDetail1>Books</CommodityDetail1>
                             <CommodityDetail2>Educational</CommodityDetail2>
                          </Commodity>
                          <ActualWeight>{order.total_weight}</ActualWeight>
                          <Dimensions>...</Dimensions>
                          <InvoiceNo>{order.number}</InvoiceNo>
                          <PackType>SPX</PackType>
                          <ProductCode>A</ProductCode> <!-- A for Air, E for ground etc. -->
                          <ProductType>Dutiables</ProductType>
                       </Services>
                    </Shipment>
                 </Request>
              </GenerateWayBill>
           </soapenv:Body>
        </soapenv:Envelope>
        """

        # 2. Make the API call
        response = requests.post(self.waybill_generation_url, data=payload.encode('utf-8'), headers=headers)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # 3. Parse the XML response to get the AWB number
        # Again, the exact tags will be in the BlueDart documentation
        root = ET.fromstring(response.content)
        awb_number = root.find('.//AWBNo').text
        
        if not awb_number:
            error_message = root.find('.//Status').text
            raise Exception(f"BlueDart API Error: {error_message}")

        # The API might also return a base64 encoded PDF for the shipping label
        label_data = root.find('.//AWBPrintContent').text

        return awb_number, label_data

    def get_tracking_info(self, awb_number):
        """
        Calls the BlueDart ShopTrack™ API to get status updates.
        This would be used for your tracking page.
        """
        # Similar to above: construct the XML payload for tracking,
        # make the request, and parse the response.
        pass

# Instantiate a single client for the app to use
bluedart_client = BlueDartClient()
