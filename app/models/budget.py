from sqlalchemy import (DECIMAL,ForeignKey,CheckConstraint,Enum as SQLENUM,DATE)
from datetime import date
from decimal import Decimal
from sqlalchemy.orm import(relationship,Mapped,mapped_column,validates)
from db.base_class import Base
from core.enums import Status
from core.validators import check_positive_number
from .category import Category

class Budget(Base):
    budget_id : Mapped[int] = mapped_column(primary_key=True)
    amount : Mapped[Decimal] =  mapped_column(DECIMAL(12,2),CheckConstraint("amount > 0"))
    category_id : Mapped[int] = mapped_column(ForeignKey("categories.category_id"))
    category : Mapped["Category"] = relationship(back_populates="category")
    start_date : Mapped[date] = mapped_column(DATE,nullable=False)
    end_date : Mapped[date] = mapped_column(DATE,CheckConstraint("end_date > start_date"),nullable=False)
    status : Mapped[Status] = mapped_column(SQLENUM(Status),nullable=False)

    @validates("amount")
    def check_budget_amount(self,amount:Decimal):
        return check_positive_number(amount)
    
    @validates("end_date")
    def check_end_date(self,end_date : date):
        if end_date < self.start_date:
            raise ValueError("Gia tri ngay ket thuc khong hop le")
        return end_date
    
