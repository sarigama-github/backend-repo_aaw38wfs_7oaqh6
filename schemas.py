"""
Database Schemas for Manufacturing Showcase

Each Pydantic model below maps to a MongoDB collection. The collection
name is the lowercase of the class name.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List


class ContactMessage(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company name")
    message: str = Field(..., description="Message body")
    source: Optional[str] = Field("contact", description="contact | quote | other")


class QuoteRequest(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company name")
    product_type: str = Field(..., description="vacbag | detergents | white-label | other")
    quantity: Optional[str] = Field(None, description="Estimated quantity or cadence")
    details: Optional[str] = Field(None, description="Project details or specifications")
    country: Optional[str] = Field(None, description="Country of the client")


class Testimonial(BaseModel):
    client: str = Field(..., description="Client name or company")
    quote: str = Field(..., description="What they said")
    sector: Optional[str] = Field(None, description="Industry sector")
    country: Optional[str] = Field(None)


class ProductHighlight(BaseModel):
    name: str = Field(...)
    brand: str = Field(..., description="Vacbag | WTF | Other")
    features: List[str] = Field(default_factory=list)
    image_url: Optional[str] = None

