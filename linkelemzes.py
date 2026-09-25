import json

class FraudLinkAnalyzer:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_entity(self, entity_id: str, entity_type: str, details: dict):
        """Hozzáad egy csomópontot (pl. számla, domain, IP) a hálózathoz."""
        self.nodes[entity_id] = {"type": entity_type, "details": details}

    def add_connection(self, source: str, target: str, relation: str):
        """Összeköti a csomópontokat (pl. utalás, domain regisztráció)."""
        self.edges.append({"source": source, "target": target, "relation": relation})

    def export_graph_report(self) -> str:
        """Exportálja a hálózati mátrixot a döntéshozók számára."""
        report = {
            "total_entities": len(self.nodes),
            "total_connections": len(self.edges),
            "network_map": {
                "nodes": self.nodes,
                "edges": self.edges
            }
        }
        return json.dumps(report, indent=4, ensure_ascii=False)

# --- Példa a hálózat építésére ---
if __name__ == "__main__":
    network = FraudLinkAnalyzer()
    
    # Entitások felvétele
    network.add_entity("domain_1", "Fraudulent Domain", {"name": "vendor-secure-update.com"})
    network.add_entity("ip_1", "Originating IP", {"address": "192.168.100.50"})
    network.add_entity("acc_1", "Mule Bank Account", {"iban": "HU12345678...TEMP"})
    
    # Kapcsolatok (élek) definiálása
    network.add_connection("ip_1", "domain_1", "HOSTS_MAIL_SERVER")
    network.add_connection("domain_1", "acc_1", "USED_IN_BEC_INVOICE")
    
    print("--- Pénzügyi Csalási Hálózati Riport ---")
    print(network.export_graph_report())
