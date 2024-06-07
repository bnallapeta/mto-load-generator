import openshift as oc
import time
import argparse
import yaml

def load_yaml_template(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file.read())

def create_tenant(tenant_name, tenant_template):
    tenant_yaml = tenant_template.format(tenant_name=tenant_name)
    with oc.project('default'):
        oc.create(yaml.safe_load(tenant_yaml))
    print(f"Tenant '{tenant_name}' created.")

def deploy_dummy_app(namespace, app_template):
    with oc.project(namespace):
        oc.create(app_template)
    print(f"Dummy app deployed in namespace '{namespace}'.")

def wait_for_namespace(namespace, retries=10, delay=5):
    for attempt in range(retries):
        try:
            with oc.project(namespace):
                print(f"Namespace '{namespace}' is ready.")
                return True
        except oc.OpenShiftPythonException:
            print(f"Waiting for namespace '{namespace}' to be created... (Attempt {attempt+1}/{retries})")
            time.sleep(delay)
    print(f"Namespace '{namespace}' creation failed after {retries} attempts.")
    return False

def main(tenant_prefix, num_tenants):
    tenant_template = load_yaml_template('templates/tenant_template.yaml')
    dummy_app_template = load_yaml_template('templates/dummy_app_template.yaml')

    for tenant_id in range(num_tenants):
        tenant_name = f"{tenant_prefix}-{tenant_id}"
        create_tenant(tenant_name, tenant_template)
        time.sleep(1)  # Small delay to avoid overwhelming the API

        # Wait for namespaces to be created by the operator
        tenant_namespaces = [f"{tenant_name}-gryffindor", f"{tenant_name}-slytherin", "hufflepuff", "ravenclaw"]
        for ns in tenant_namespaces:
            if wait_for_namespace(ns):
                deploy_dummy_app(ns, dummy_app_template)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate tenants and namespaces on OpenShift.")
    parser.add_argument('--tenant-prefix', type=str, required=True, help='Prefix for tenant names')
    parser.add_argument('--num-tenants', type=int, required=True, help='Number of tenants to create')
    args = parser.parse_args()

    main(args.tenant_prefix, args.num_tenants)
