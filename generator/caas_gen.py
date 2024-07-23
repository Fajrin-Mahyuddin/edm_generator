from data import data, url_assets, data_no_rsvp, data_caas_edm
from generator_for_caas import get_b64_img, generate_html
import sys

# f = open("result/invitation-edm.html", "w")
args = sys.argv
asset_type = "url"
filetypes = "html"
assets = url_assets

# if len(args) > 2:
# 	asset_type = check_assets_type(args[1])
# 	filetypes = args[2]
# elif len(args) > 1:    
# 	asset_type = check_assets_type(args[1])
# else:
# 	print("generating file using url assets and html files !...")
	
# if asset_type == "base64":
assets = get_b64_img()
	
if(assets and data_caas_edm):
	for item in data_caas_edm: 
		generate_html(item, assets)
	print("generate success !")
else:
  print("failed generating file !")




# f.write(html_sintax)
# f.close()
