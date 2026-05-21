from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

# -----------------------------------------
# Modelo Obra
# -----------------------------------------

class Obra(Base):
    __tablename__ = "obras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    # Relación uno a muchos
    presupuestos: Mapped[list["Presupuesto"]] = relationship(
        back_populates="obra",
        cascade="all, delete-orphan"
    )