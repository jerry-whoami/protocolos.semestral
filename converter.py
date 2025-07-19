from ncclient import manager

filter = """
<filter type="subtree">
  <ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state><ospf-instance><ospf-area><ospf-interface>
      <name/><adjacency-information><neighbors>
        <neighbor>
          <neighbor-id/>
          <neighbor-address/>
          <neighbor-state/>
          <is-adjacency-full/>
        </neighbor>
      </neighbors></adjacency-information>
    </ospf-interface></ospf-area></ospf-instance></ospf-state>
  </ospf-oper-data>
</filter>
"""

with manager.connect(host="x.x.x.x", port=830,
                     username="...", password="...",
                     hostkey_verify=False) as m:
    resp = m.get(filter)
    print(resp.xml)

