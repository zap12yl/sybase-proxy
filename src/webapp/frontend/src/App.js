// src/webapp/frontend/src/App.js
import React, { useState } from "react";
import axios from "axios";

function App() {
  const [adConfig, setAdConfig] = useState({
    ad_server: "",
    ad_domain: "",
    ad_base_dn: "",
  });
  const [dbConfig, setDbConfig] = useState({
    pg_host: "",
    pg_port: 5432,
    pg_user: "",
    pg_password: "",
    pg_db: "",
  });
  const [roleMapping, setRoleMapping] = useState({
    ad_group: "",
    pg_role: "",
  });

  const saveAdConfig = async () => {
    await axios.post("/config/ad", adConfig);
    alert("AD configuration saved!");
  };

  const saveDbConfig = async () => {
    await axios.post("/config/db", dbConfig);
    alert("Database configuration saved!");
  };

  const saveRoleMapping = async () => {
    await axios.post("/config/roles", roleMapping);
    alert("Role mapping saved!");
  };

  return (
    <div>
      <h1>Proxy Configuration</h1>
      <div>
        <h2>AD Configuration</h2>
        <input
          placeholder="AD Server"
          value={adConfig.ad_server}
          onChange={(e) => setAdConfig({ ...adConfig, ad_server: e.target.value })}
        />
        <input
          placeholder="AD Domain"
          value={adConfig.ad_domain}
          onChange={(e) => setAdConfig({ ...adConfig, ad_domain: e.target.value })}
        />
        <input
          placeholder="AD Base DN"
          value={adConfig.ad_base_dn}
          onChange={(e) => setAdConfig({ ...adConfig, ad_base_dn: e.target.value })}
        />
        <button onClick={saveAdConfig}>Save</button>
      </div>
      <div>
        <h2>Database Configuration</h2>
        <input
          placeholder="PostgreSQL Host"
          value={dbConfig.pg_host}
          onChange={(e) => setDbConfig({ ...dbConfig, pg_host: e.target.value })}
        />
        <input
          placeholder="PostgreSQL Port"
          value={dbConfig.pg_port}
          onChange={(e) => setDbConfig({ ...dbConfig, pg_port: e.target.value })}
        />
        <input
          placeholder="PostgreSQL User"
          value={dbConfig.pg_user}
          onChange={(e) => setDbConfig({ ...dbConfig, pg_user: e.target.value })}
        />
        <input
          placeholder="PostgreSQL Password"
          type="password"
          value={dbConfig.pg_password}
          onChange={(e) => setDbConfig({ ...dbConfig, pg_password: e.target.value })}
        />
        <input
          placeholder="PostgreSQL Database"
          value={dbConfig.pg_db}
          onChange={(e) => setDbConfig({ ...dbConfig, pg_db: e.target.value })}
        />
        <button onClick={saveDbConfig}>Save</button>
      </div>
      <div>
        <h2>Role Mapping</h2>
        <input
          placeholder="AD Group"
          value={roleMapping.ad_group}
          onChange={(e) => setRoleMapping({ ...roleMapping, ad_group: e.target.value })}
        />
        <input
          placeholder="PostgreSQL Role"
          value={roleMapping.pg_role}
          onChange={(e) => setRoleMapping({ ...roleMapping, pg_role: e.target.value })}
        />
        <button onClick={saveRoleMapping}>Save</button>
      </div>
    </div>
  );
}

export default App;
