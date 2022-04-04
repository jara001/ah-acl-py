#!/usr/bin/env python3
# client_pkcs12.py
"""Arrowhead Client class using .p12 certificates.
"""

from aclpy.client.client import ArrowheadClient as ArrowheadClientBase
from aclpy.connector.connector_pkcs12 import ArrowheadConnector
from aclpy.server import ArrowheadServer


class ArrowheadClient(ArrowheadClientBase):
    """ArrowheadClient class for utilizing pkcs12 to communicate with Arrowhead Core.

    Additional attributes:
    p12file (str) -- path to the .p12 certificate
    p12pass (str) -- password to the .p12 certificate
    pubfile (str) -- path to the public key .pub
    cafile (str) -- path to the certificate authority file .ca
    server (ArrowheadServer) -- configuration of the Arrowhead Core server
    """

    def __init__(self, *,
            name: str,
            address: str,
            port: int,
            p12file: str,
            p12pass: str,
            pubfile: str,
            cafile: str,
            server: ArrowheadServer
    ):
        """Initialize ArrowheadClient class."""
        # Read pubkey first
        with open(pubfile, "r") as f:
            pubkey = f.read()

        self.connector = ArrowheadConnector(server)

        super(ArrowheadClient, self).__init__(name, address, port, pubkey.replace("\n", ""), self.connector)

        self.p12file = p12file
        self.p12pass = p12pass
        self.pubfile = pubfile
        self.cafile = cafile
